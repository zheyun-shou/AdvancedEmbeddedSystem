#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xcb440b5e, "module_layout" },
	{ 0x1fb863c1, "usb_serial_generic_tiocmiwait" },
	{ 0x5cdf07ef, "usb_serial_deregister_drivers" },
	{ 0xb6dc3b67, "usb_serial_register_drivers" },
	{ 0xbd19e47d, "tty_kref_put" },
	{ 0x152ceeda, "usb_serial_handle_dcd_change" },
	{ 0x3946fdda, "tty_port_tty_get" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0x9ae96f87, "usb_serial_generic_resume" },
	{ 0x7f793f98, "usb_serial_generic_open" },
	{ 0x2ad31def, "usb_submit_urb" },
	{ 0x37befc70, "jiffies_to_msecs" },
	{ 0x54496b4, "schedule_timeout_interruptible" },
	{ 0xd597e201, "tty_put_char" },
	{ 0x15ba50a6, "jiffies" },
	{ 0xe2cf86c7, "_dev_info" },
	{ 0x8bd65ff4, "kmem_cache_alloc_trace" },
	{ 0xc83492ef, "kmalloc_caches" },
	{ 0x30e74134, "tty_termios_copy_hw" },
	{ 0x409873e3, "tty_termios_baud_rate" },
	{ 0x6c257ac0, "tty_termios_hw_change" },
	{ 0x82017c89, "usb_kill_urb" },
	{ 0xdc60224b, "usb_serial_generic_close" },
	{ 0x37a0cba, "kfree" },
	{ 0x72839fb4, "_dev_err" },
	{ 0xfbec9cee, "usb_control_msg" },
	{ 0xcf6cc643, "__dynamic_dev_dbg" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "usbserial");

MODULE_ALIAS("usb:v1A86p5512d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v1A86p5523d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v1A86p7522d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v1A86p7523d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v4348p5523d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v9986p7523d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "A5CE568BF3469EF2BA8D2CD");
