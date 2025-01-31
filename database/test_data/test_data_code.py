import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not -2486340971361125775 in succeeded_hashes:  # avoid duplicate inserts
            instance = product1 = Product(id=1, description='Smartphone', photo_url='http://example.com/smartphone.jpg', unit_type='unit')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2486340971361125775)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1677244399615775863 in succeeded_hashes:  # avoid duplicate inserts
            instance = product2 = Product(id=2, description='Laptop', photo_url='http://example.com/laptop.jpg', unit_type='unit')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1677244399615775863)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8380941964507827688 in succeeded_hashes:  # avoid duplicate inserts
            instance = product3 = Product(id=3, description='Milk', photo_url='http://example.com/milk.jpg', unit_type='liter')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8380941964507827688)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2303895827968951224 in succeeded_hashes:  # avoid duplicate inserts
            instance = product4 = Product(id=4, description='Bread', photo_url='http://example.com/bread.jpg', unit_type='unit')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2303895827968951224)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6522662178035957382 in succeeded_hashes:  # avoid duplicate inserts
            instance = variant1 = ProductVariant(id=1, product_id=1, size='Large', color='Black')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6522662178035957382)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5786702401260771947 in succeeded_hashes:  # avoid duplicate inserts
            instance = variant2 = ProductVariant(id=2, product_id=2, size='15-inch', color='Silver')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5786702401260771947)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5984765309767266738 in succeeded_hashes:  # avoid duplicate inserts
            instance = variant3 = ProductVariant(id=3, product_id=3, size='1-liter', color='White')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5984765309767266738)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3328139654402572611 in succeeded_hashes:  # avoid duplicate inserts
            instance = variant4 = ProductVariant(id=4, product_id=4, size='Medium', color='Brown')
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3328139654402572611)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4186226608261066272 in succeeded_hashes:  # avoid duplicate inserts
            instance = transaction1 = ProductTransaction(id=1, product_id=1, transaction_type='sale', quantity=5, transaction_date=datetime(2023, 10, 5))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4186226608261066272)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5989919845903583673 in succeeded_hashes:  # avoid duplicate inserts
            instance = transaction2 = ProductTransaction(id=2, product_id=2, transaction_type='purchase', quantity=8, transaction_date=datetime(2023, 10, 6))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5989919845903583673)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5916827897982701178 in succeeded_hashes:  # avoid duplicate inserts
            instance = transaction3 = ProductTransaction(id=3, product_id=3, transaction_type='sale', quantity=10, transaction_date=datetime(2023, 10, 7))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5916827897982701178)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4381203536421142979 in succeeded_hashes:  # avoid duplicate inserts
            instance = transaction4 = ProductTransaction(id=4, product_id=4, transaction_type='purchase', quantity=2, transaction_date=datetime(2023, 10, 8))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4381203536421142979)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
