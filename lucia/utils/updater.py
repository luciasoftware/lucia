import webbrowser, urllib.request

# usage
# u = Updater(current_version_string, url_to_remote_version.txt, url_to_where_the_download_can_be_installed)
# u.checkForUpdates() # queries the remote server for a new version.
# If above call returns true call u.performUpdate().
class Updater:
	def __init__(self, version, version_url, download_url):
		self.version = version
		self.version_url = version_url
		self.download_url = download_url

	def check_for_updates(self, debug=True):
		try:
			with urllib.request.urlopen(self.version_url) as url:
				new_version = url.read()
			if str(self.version) != new_version.decode():
				self.new_version = new_version.decode()
				return True
			else:
				return False
		except:
			print("Error checking for updates.")
			return False

	def perform_update(self):
		webbrowser.open(self.download_url)

	def get_new_version(self):
		return self.new_version
