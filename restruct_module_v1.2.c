#include "asterisk.h"

AST_MODULE_INFO_STANDARD(ASTERISK_GPL_KEY, "My Custom Asterisk Module");

static const char *description = "My Custom Asterisk Module";

static int my_module_load(void) {
    /* Add any initialization code for the module here */
    return AST_MODULE_LOAD_SUCCESS;
}

static int my_module_unload(void) {
    /* Add any cleanup code for the module here */
    return 0;
}

static const struct ast_module_info my_module_info = {
    .name = AST_MODULE_SELF_SYM,
    .flags = AST_MODFLAG_LOAD_ORDER,
    .description = description,
    .load = my_module_load,
    .unload = my_module_unload,
};

AST_MODULE_INFO(ASTERISK_GPL_KEY, AST_MODFLAG_DEFAULT, &my_module_info);
