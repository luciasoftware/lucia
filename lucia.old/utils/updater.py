# Copyright (C) 2018  LuciaSoftware and it's contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.

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
