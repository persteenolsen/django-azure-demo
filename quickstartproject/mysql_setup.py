# 22-10-2025 - Enable and needed only if using a virtual invironnment + MySQL
import pymysql

pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.install_as_MySQLdb()