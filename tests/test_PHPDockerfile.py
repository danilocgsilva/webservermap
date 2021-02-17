import unittest
import sys
sys.path.insert(1, "..")
from webservermap.PHPDockerfile import PHPDockerfile
from tests.assets.phpdockerfull_content import getContent as getcontentFull
from tests.assets.phpdockerprod_content import getContent as getcontentProd

class test_PHPDockerfile(unittest.TestCase):

    def test_full_dev_dockerfile_php(self):
        phpDockerFile = PHPDockerfile()
        expectedContent = getcontentFull()
        returnedContent = phpDockerFile.getPHPDockerFileContentDev()
        self.assertEqual(expectedContent, returnedContent)

    def test_prod_dockerfile_php(self):
        phpDockerFile = PHPDockerfile()
        expectedContent = getcontentProd()
        returnedContent = phpDockerFile.getPHPDockerFileContentDev()
        self.assertEqual(expectedContent, returnedContent)
