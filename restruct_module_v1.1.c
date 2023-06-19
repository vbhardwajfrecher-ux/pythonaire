#include <stdio.h>

#define MAX_LINE_LENGTH 1024

void parse_log_file(const char *filename) {
    FILE *fp;
    char line[MAX_LINE_LENGTH];

    fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error opening log file.\n");
        return;
    }

    while (fgets(line, MAX_LINE_LENGTH, fp) != NULL) {
        // Process the current log line as needed
        if (strstr(line, "autodestruct") != NULL) {
            // Perform action when "autodestruct" message is found
            printf("Found autodestruct message: %s", line);
        }
    }

    fclose(fp);
}
