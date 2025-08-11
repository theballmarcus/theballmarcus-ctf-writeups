#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void setup(void) {
    printf("/ᐠ˵- ⩊ -˵マ Mreoow!! Hey häcker can you help me find the vETenarian?\n");
    printf("ദ്ദി/ᐠ｡‸｡ᐟ\\   I remember it being hidden in one of these files...\n");
}

int is_safe_filename(const char *s) {
    for (size_t i = 0; s[i]; i++)
        if (!isalnum(s[i]) && s[i] != '.' && s[i] != '/' && s[i] != '_' && s[i] != ' ')
            return 0;
    return 1;
}

void run_cat(const char *input) {
    char cat_flags[4] = "n";
    char filename[100];
    char cmd[100] = "";
    if (!is_safe_filename(input)) {
        printf("/ᐠ - ˕ -マ I don't think the vETenarian is over there hooman...\n");
        return;
    }
    strcpy(filename, input);
    snprintf(cmd, sizeof(cmd), "cat -%s %s", cat_flags, filename);
    system(cmd);
}

int main(void) {
    char cmdline[0x100];
    setup();

    while (1) {
        printf("> ");
        fflush(stdout);
        if (!fgets(cmdline, sizeof(cmdline), stdin)) break;

        size_t len = strlen(cmdline);
        if (len > 0 && cmdline[len - 1] == '\n') cmdline[len - 1] = '\0';

        if (strncmp(cmdline, "cat ", 4) == 0) {
            run_cat(cmdline + 4);
        } else if (strcmp(cmdline, "exit") == 0) {
            printf("/ᐠ>ヮ<ᐟ\\ฅ Goodbye!\n");
            break;
        } else if (strcmp(cmdline, "") != 0) {
            printf("/ᐠ • ˕ •マ ? Unknown command: %s\n", cmdline);
            printf("Try: cat <filename> or exit\n");
        }
    }

    return 0;
}
