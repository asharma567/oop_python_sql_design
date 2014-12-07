import sqlite3
import itertools
"""
Performance Class
"""

class Performance(object):
    """
    Performance is a class for figuring out performance metrics of the solar systems
    that are in performance db:
        TABLES: FIELD NAMES
        data: systemid, datatime, actualkwh, expectedkwh
        systems: systemid, name
    """
    conn = sqlite3.connect('performance.db')
    cur = conn.cursor()

    def __init__(self, systemname):
        """
        NOTE: only successfully instatiated if pass a valid system name
        INPUT: systemname
        OUTPUT: instatiated object with valid system name
        """

        #VALIDATION: checks systemname vs all names currently within the database
        if systemname in Performance.names():
            self.systemname = systemname
        else:
            raise NameError(systemname + ' does not exist')
        pass

    @classmethod
    def names(cls):
        """
        INPUT: query to performance.db of all names of systems
        OUTPUT: all names of systems
        """

        cls.cur.execute('SELECT name FROM systems;')
        names = cls.cur.fetchall()
        set_of_names = map(str, list(itertools.chain(*names)))

        return set_of_names

    def name(self):
        """
        OUTPUT: system name of obj
        """

        return self.systemname

    def lifetimeperformance(self):
        """
        OUTPUT: lifetimeperformance = sum(actualkwh) / sum(expectedkwh)
        """
        lifetimeperformance_query_string = '''
        SELECT sum(actualkwh) / sum(expectedkwh)
        FROM data as d, systems as s
        WHERE d.systemid == s.systemid
            AND s.name = ?
        '''
        self.cur.execute(lifetimeperformance_query_string, (self.systemname,))

        #should probably write a utility function which unpacks [(x,)]
        return self.cur.fetchall()[0][0]

    def __del__(self):
        self.conn.close()

