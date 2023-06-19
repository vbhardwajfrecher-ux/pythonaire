#include "asterisk.h"

ASTERISK_FILE_VERSION(__FILE__, "$Revision: 1.0 $")

static const char * const ast_module[] = {
    "autoload",
    NULL
};

static int autodestruct_handler(int fd, int timeout, void *user_data)
{
    char buffer[1024];
    int read_count = 0;
    int autodestruct_found = 0;
    FILE *fp;
    
    /* Open the Asterisk log file for reading */
    fp = fopen("/var/log/asterisk/messages", "r");
    if (!fp) {
        ast_log(LOG_WARNING, "Could not open Asterisk log file\n");
        return -1;
    }
    
    /* Read the log file line by line */
    while (fgets(buffer, sizeof(buffer), fp)) {
        /* Check if the "autodestruct" message is present */
        if (strstr(buffer, "autodestruct") != NULL) {
            autodestruct_found = 1;
            break;
        }
        read_count++;
    }
    
    /* Close the log file */
    fclose(fp);
    
    /* Restart the Asterisk service if the "autodestruct" message was found */
    if (autodestruct_found) {
        ast_log(LOG_WARNING, "Restarting Asterisk service\n");
        system("service asterisk restart");
    }
    
    /* Return the number of lines read from the log file */
    return read_count;
}

static struct ast_custom_function autodestruct_function = {
    .name = "AUTODESTRUCT",
    .synopsis = "Detects the 'autodestruct' message in the Asterisk log file and restarts the Asterisk service",
    .syntax = "",
    .read = autodestruct_handler,
    .desc =
    "This function reads the Asterisk log file and searches for the 'autodestruct' message. If the message is found, the function\n"
    "restarts the Asterisk service to prevent any further issues. The function returns the number of lines read from the log file.\n",
};

static int load_module(void)
{
    ast_custom_function_register(&autodestruct_function);
    return AST_MODULE_LOAD_SUCCESS;
}

static int unload_module(void)
{
    ast_custom_function_unregister(&autodestruct_function);
    return 0;
}

AST_MODULE_INFO_STANDARD(ASTERISK_GPL_KEY, "Custom Asterisk module for autodestruct detection and resolver");
