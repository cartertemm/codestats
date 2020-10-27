import os

languages = []


class language:
	def __init__(self, name, extensions, parent_lang="", associated_files=[]):
		self.name = name
		self.extensions = extensions
		self.associated_files = associated_files
		self.parent_lang = parent_lang
		languages.append(self)

	def __str__(self):
		final = self.name
		if self.parent_lang:
			final += " (" + self.parent_lang + ")"
		return final


# here we keep the data for all known languages
# todo: possibly integrate with a database (linguist) for more accurate results
# note: the following was mostly generated with a script. I've attempted to clean it up but might have missed something.

language("AngelScript", [".as", ".angelscript"], "C++")
language(
	"ApacheConf",
	[".apacheconf", ".vhost"],
	associated_files=[".htaccess", "apache2.conf", "httpd.conf"],
)
language("Apollo Guidance Computer", [".agc"], "assembly_x86")
language("AppleScript", [".scpt", ".applescript"])
language("ASP", [".asp", ".aspx", ".asax", ".ascx", ".ashx", ".asmx", ".axd"])
language("assembly", [".asm", ".a51", ".inc", ".nasm"])
language("AutoHotkey", [".ahk", ".ahkl"])
language("autoit", [".au3"])
language("batchfile", [".bat", ".cmd"])
language("BGT", [".bgt"])
language("brainfuck", [".bf", ".b"])
language("C/C++", [".c", ".cpp", ".c++", ".cc", ".cxx", ".h", ".hpp", ".h++", ".hxx"])
# thanks Ty
language("C# (CSharp)", [".cs", ".csx", ".cake"])
# language("chuck", (".ck"))
language("CSS", [".css"])
language("CSV", [".csv"])
language("cython", [".pyx", ".pxd", ".pyi"])
language("dockerfile", [".dockerfile"], associated_files=["dockerfile"])
language("F#", [".fs", ".fsi", ".fsx"])
language("go", [".go"])
language("HTML", [".html", ".htm", ".html.hl", ".xht", ".xhtml"])
language("HTML+Django", [".jinja", ".jinja2", ".mustache", ".njk"])
language("HTML+ERB", [".erb", ".erb.deface"])
language("HTML+PHP", [".phtml"])
language("HTTP", [".http"])
language(
	"INI",
	[".ini", ".cfg", ".lektorproject", ".prefs", ".pro", ".properties"],
	associated_files=[".editorconfig", ".gitconfig", "buildozer.spec"],
)
language("Inno Setup", [".iss"])
language("java", [".java"])
language("java server pages", [".jsp"])
language(
	"javascript",
	[
		".js",
		"._js",
		".bones",
		".es",
		".es6",
		".frag",
		".gs",
		".jake",
		".jscad",
		".jsfl",
		".jsm",
		".mjs",
		".njs",
		".pac",
		".sjs",
		".ssjs",
		".xsjs",
		".xsjslib",
	],
)
language("jaws script", [".jsb", ".jss"])
language("LOLCode", [".lol"])
language("Linux Kernel Module", [".mod"])
language("lua", [".lua", ".wlua"])
language(
	"makefile",
	[".mak", ".make", ".mk", ".mkfile"],
	associated_files=[
		"BSDmakefile",
		"GNUmakefile",
		"Kbuild",
		"Makefile",
		"Makefile.am",
		"Makefile.boot",
		"Makefile.frag",
		"Makefile.in",
		"Makefile.inc",
		"Makefile.wat",
		"makefile",
		"makefile.sco",
		"mkfile",
	],
)
language(
	"markdown",
	[
		".md",
		".markdown",
		".mdown",
		".mdwn",
		".mkd",
		".mkdn",
		".mkdown",
		".ronn",
		".workbook",
	],
	parent_lang="text",
)
language("moo", [".moo"])
language("Nmap Scripting Engine", [".nse"], parent_lang="lua")
language("NSIS", [".nsi", ".nsh"])
language("Nginx", [".nginxconf"], associated_files=["nginx.conf"])
language("PHP", [".php", ".php3", ".php4", ".php5", ".phps", ".phpt"])
language(
	"Perl",
	[".pl", ".al", ".perl", ".plx", ".pm"],
	associated_files=["Makefile.PL", "rexfile", "ack", "cpanfile"],
)
language("Powershell", [".ps1", ".psd1", ".psm1"])
language("PureBasic", [".pb", ".pbi"])
language(
	"python",
	[".py", ".pyw", ".py2", ".py3", ".pyi", ".pip"],
	associated_files=[
		".gclient",
		"BUCK",
		"BUILD",
		"BUILD.bazel",
		"SConscript",
		"SConstruct",
		"Snakefile",
		"WORKSPACE",
		"wscript",
	],
)
language("Regular Expression", [".regexp", ".regex"])
language(
	"ruby",
	[
		".rb",
		".builder",
		".eye",
		".gemspec",
		".god",
		".jbuilder",
		".mspec",
		".pluginspec",
		".podspec",
		".rabl",
		".rake",
		".rbuild",
		".rbw",
		".rbx",
		".ruby",
		".thor",
		".watchr",
	],
	associated_files=[
		".irbrc",
		".pryrc",
		"Appraisals",
		"Berksfile",
		"Brewfile",
		"Buildfile",
		"Capfile",
		"Dangerfile",
		"Deliverfile",
		"Fastfile",
		"Gemfile",
		"Gemfile.lock",
		"Guardfile",
		"Jarfile",
		"Mavenfile",
		"Podfile",
		"Puppetfile",
		"Rakefile",
		"Snapfile",
		"Thorfile",
	],
)
language("rust", [".rs", ".rs.in"])
language(
	"shell script",
	[".sh", ".bash", ".ksh", ".sh.in", ".tmux", ".zsh"],
	associated_files=[
		".bash_logout",
		".bash_profile",
		".bashrc",
		".login",
		".profile",
		".zlogin",
		".zlogout",
		".zprofile",
		".zshenv",
		".zshrc",
	],
)
language("swift", [".swift"])
language(
	"visual basic", [".vb", ".bas", ".cls", ".frm", ".frx", ".vba", ".vbhtml", ".vbs"]
)
language("windows registry entry", [".reg"])


def detect_lang(filename):
	file_ext = os.path.splitext(filename)[1]
	for i in languages:
		if file_ext in i.extensions:
			return i
		if filename in i.associated_files:
			return i
