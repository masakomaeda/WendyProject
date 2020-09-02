#include <julius/juliuslib.h>
int
get_plugin_info(int opcode, char *buf, int buflen)
{
  switch(opcode) {
  case 0:
    strncpy(buf, "start/stop notify plugin", buflen);
    break;
  }
  return 0;
}
static void
func_begin(Recog *recog, void *dummy)
{
  printf("[BEGIN]\n");
}
static void
func_end(Recog *recog, void *dummy)
{
  printf("[END]\n");
}
int
startup(void *data)
{
  Recog *recog = data;
  callback_add(recog, CALLBACK_EVENT_RECOGNITION_BEGIN, func_begin, NULL);
  callback_add(recog, CALLBACK_EVENT_RECOGNITION_END, func_end, NULL);
  return 0;
}
