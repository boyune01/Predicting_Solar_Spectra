"""
Test function
"""
import os
import unittest
from code import clean_input_data

data_dir = "/Volumes/GoogleDrive/My Drive/COURSES/22 AU/CSE_583/final_prj/data/raw/"


class UnitTests(unittest.TestCase):
<<<<<<< HEAD
    def smoke_test_read_wea_datas(self):
        """
        smoke test to check for file_dir exists.
        """
        with self.assertRaises(FileNotFoundError):
            
        return

    def edge_test_read_wea_datas(self):
=======
    def test_read_wea_datas_smoke(self):
        """
        Smoke test to check the function runs.
        """
        file_dir = data_dir
        clean_input_data(file_dir, 'wea')
        
        return
    
    def test_read_wea_datas_edge1(self):
>>>>>>> e6dc182c2c328896ca1966757eb86587862523ad
        """
        Edge test to test for .csv format
        """
        with self.assertRaises(TypeError):
<<<<<<< HEAD
            for file in files:  # Q: WE WANT TO CHECK 'FILES' WHICH IS A VALUE INSIDE 'READ_WEA_DATAS' FUNCTION. HOW DO WE ACCESS A VALUE INSIDE A FUNCTION?
                # Split the extension from the path and normalise it to lowercase.
                ext = os.path.splitext(file)[-1].lower()
                if ext == ".csv":
                    pass
=======
            file_dir = "...."
            clean_input_data(file_dir, 'wea')
>>>>>>> e6dc182c2c328896ca1966757eb86587862523ad
        
        return

    def 
