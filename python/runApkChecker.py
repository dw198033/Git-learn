import subprocess

class PerformRunControl():

    def __init__(self, cmd):
        """
        初始化函数，接受控制空规格内存的5个参数
        """
        self.cmd = cmd

    def runCmd(self, cmd):
        """运行命令
        """
        print("  --runCmd: " + cmd)
        pCmd = subprocess.Popen(cmd, \
                                shell = True, \
                                stdout = subprocess.PIPE, \
                                stderr = subprocess.STDOUT)
        output, unused_err = pCmd.communicate()
        return pCmd, output

    def run(self):
        """
        运行总入口函数
        """
        result = True
        runResult, output = self.runCmd(self.cmd)
        if runResult.returncode == 0:
            result = True
            print("  --Run Success.")
        else:
            result = False
            print("  --Run Fail")
        try:
            for lineStr in output.decode('UTF-8', 'ignore').split("\n"):
                #209 tests completed, 1 failed
                print("  --> " + lineStr)
        except Exception as err:
            print(err)
        return result

if __name__ == '__main__':

    # testCmd = "java -jar matrix-apk-canary-0.4.10.jar --config config.json"    
    testCmd = "python vs_test2.py"
	
    control = PerformRunControl(testCmd)
    control.run()