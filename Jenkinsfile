node {
    properties([
        pipelineTriggers([
            cron('H 4 * * 1-5')
        ])
    ])

    def branchName = env.BRANCH_NAME
    def workspace = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\"

    try {
        stage("Clearing Workspace") {

def branchesToExclude = ["main","feature1","feature2","feature3"]

            if (branchesToExclude.contains(branchName)) {
                echo "No need to delete the workspace"
            } else {
                dir(workspace) {
                    deleteDir()
                }
            }
        }
    } catch (Exception e) 
    {
        echo "Encountered an exception"
        echo e.toString()
    }
}
