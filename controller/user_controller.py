from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from fastapi import HTTPException

engine = create_engine('mysql+pymysql://root:root@localhost/mydemodb')
Session = sessionmaker(bind=engine)

def get_db_session():
    return Session()

def save(user: User):
    session = get_db_session()
    try:
        session.add(user)
        session.commit()
        return user
    except Exception as e:
       raise HTTPException(status_code=400, detail="User Id is already exists")
    finally:
        session.close()

def update(user: User):
    session = get_db_session()
    try:
        session.merge(user)
        session.commit()
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        session.close()
    return False

def delete(id: int):
    session = get_db_session()
    try:
        user = session.query(User).filter_by(id=id).first()
        print("1")
        if user:
            session.delete(user)
            session.commit()
            return True
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        session.close()
    return False

def read(id: int = None):
    session = get_db_session()
    try:
        if id is None:
            users = session.query(User).all()
            return users
        else:
            user = session.query(User).filter_by(id=id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return [user]
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")
    finally:
        session.close()

def check_duplicate_id(id: int) -> bool:
    session = get_db_session()
    try:
        user = session.query(User).filter_by(id=id).first()
        return user is not None
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        session.close()
