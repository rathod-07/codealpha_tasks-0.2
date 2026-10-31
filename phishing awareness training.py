"""Slide-by-slide content for a phishing awareness training presentation."""

SLIDES = [
	{
		"title": "Phishing Awareness Training",
		"subtitle": "CodeAlpha Cyber Security Internship",
		"content": [
			"Recognize suspicious messages before they cause harm.",
			"Pause • Check • Verify • Report",
		],
		"speaker_notes": (
			"Welcome participants. Explain that phishing can target anyone, "
			"and that careful verification is more reliable than judging a "
			"message by its appearance alone."
		),
	},
	{
		"title": "What Is Phishing?",
		"content": [
			"Phishing is a form of social engineering in which an attacker "
			"pretends to be a trusted person or organization.",
			"Goals: steal passwords or payment details, obtain sensitive "
			"information, deliver malware, or persuade someone to send money.",
			"Email phishing: broad or mass email messages pretending to be "
			"legitimate.",
			"Spear phishing (sometimes mistakenly called “spearfishing”): "
			"a personalized message aimed at a specific person or group.",
			"Smishing: phishing delivered by SMS or text message.",
		],
		"speaker_notes": (
			"Attackers commonly create pressure or impersonate familiar "
			"brands and colleagues. A message can be fraudulent even if it "
			"contains a real name, logo, or relevant detail."
		),
	},
	{
		"title": "How to Identify Phishing Emails",
		"content": [
			"Sender address: inspect the full address and domain; watch for "
			"look-alike spellings or unrelated domains.",
			"Greeting: generic openings or an unexpected lack of context "
			"may be warning signs.",
			"Urgent or threatening tone: “act now,” account closure, or "
			"unexpected prizes are used to rush decisions.",
			"Links: hover to preview the destination on a computer; on a "
			"phone, press and hold only if safe to preview. Do not open "
			"unexpected links.",
			"Attachments: be cautious with unexpected files, especially "
			"those asking you to enable macros or sign in.",
			"Mismatched details, unusual requests, spelling issues, or "
			"requests to bypass normal procedures can be clues.",
		],
		"speaker_notes": (
			"One clue alone does not prove a message is malicious, and "
			"polished messages can still be phishing. Verify unusual "
			"requests using a known phone number, official website, or "
			"separate trusted communication channel."
		),
	},
	{
		"title": "Example: A Fake Bank Login Email",
		"content": [
			"Subject: “URGENT: Your account will be locked today!”",
			"Sender display name: “Example Bank Security”; full address: "
			"security@example-alert.invalid",
			"Message: “Dear Customer, unusual activity was detected. "
			"Confirm your account immediately using the button below.”",
			"Button label: “Verify Account”; displayed destination: "
			"https://example.invalid/verify",
			"Visual indicators: generic greeting, pressure, unfamiliar "
			"sender domain, and a link that is not the bank's known domain.",
			"Safe response: do not click or reply. Open the bank's official "
			"app/site yourself or call the number printed on your card; "
			"report the message through your organization's process.",
		],
		"speaker_notes": (
			"This is a fictional example using reserved .invalid domains. "
			"Ask the audience to name the warning signs before revealing "
			"the analysis. Logos and button styling do not establish trust."
		),
	},
	{
		"title": "Best Practices for Prevention",
		"content": [
			"Enable multi-factor authentication (MFA/2FA), preferably a "
			"passkey or authenticator method where available.",
			"Verify URLs and sign in through a saved bookmark or by typing "
			"the known official address yourself.",
			"Use a password manager and unique passwords for every account; "
			"never share one-time codes or approve unexpected sign-in prompts.",
			"Confirm payment, password-reset, or sensitive-data requests "
			"through a separate trusted channel.",
			"Report suspicious messages using your organization's phishing "
			"report button or IT/security team. Do not forward risky links "
			"to coworkers.",
			"If you clicked or shared information, report it immediately, "
			"change affected credentials through the official site, and "
			"follow your organization's incident guidance.",
		],
		"speaker_notes": (
			"MFA adds protection but cannot make every attack impossible. "
			"Prompt reporting helps security teams protect other users; "
			"employees should not be blamed for reporting a mistake quickly."
		),
	},
	{
		"title": "Interactive Quiz",
		"content": [
			"1. An email says your account will close unless you sign in "
			"through its link. What should you do?",
			"   A) Click quickly   B) Visit the official site independently "
			"and report the email   C) Reply with your password",
			"   Answer: B — avoid the message link and verify through an "
			"official channel.",
			"2. What is smishing?",
			"   A) Phishing by SMS/text   B) A secure password method "
			"  C) A software update",
			"   Answer: A — smishing is phishing delivered by text message.",
			"3. A colleague urgently requests a payment change by email. "
			"What is safest?",
			"   A) Pay immediately   B) Reply to the same email only "
			"  C) Confirm using a known, separate contact method",
			"   Answer: C — independently verify unexpected sensitive requests.",
		],
		"speaker_notes": (
			"Let participants choose before showing each answer. Reinforce "
			"the core habit: stop, inspect, verify independently, and report."
		),
	},
]


def print_presentation():
	"""Print the slide content and speaker notes in a readable format."""
	for number, slide in enumerate(SLIDES, start=1):
		print("\n" + "=" * 72)
		print("SLIDE " + str(number) + ": " + slide["title"])
		print("=" * 72)

		subtitle = slide.get("subtitle")
		if subtitle:
			print(subtitle)

		for item in slide["content"]:
			print("• " + item)

		print("\nSpeaker notes: " + slide["speaker_notes"])


if __name__ == "__main__":
	print_presentation()
