local lfs = require("lfs") -- LuaFileSystem for directory listing

-- Function to list all audio files in the current directory
local function list_audio_files()
	local audio_files = {}
	for file in lfs.dir(".") do
		if file:match("%.mp3$") or file:match("%.wav$") or file:match("%.ogg$") then
			table.insert(audio_files, file)
		end
	end
	return audio_files
end

-- Function to display options
local function show_menu(files)
	print("===== Terminal Music Player =====\n")
	for i, file in ipairs(files) do
		print(string.format("%d. %s", i, file))
	end
	print("\nOptions:")
	print("1. Play Music")
	print("2. Exit")
end

-- Main function
local function main()
	local audio_files = list_audio_files()

	if #audio_files == 0 then
		print("No audio files found in the current directory.")
		return
	end

	while true do
		show_menu(audio_files)
		io.write("\nEnter your choice: ")
		local choice = io.read()

		if choice == "1" then
			io.write("\nEnter the number of the music file to play: ")
			local index = tonumber(io.read())

			if index and index >= 1 and index <= #audio_files then
				local file = audio_files[index]
				print("\nPlaying: " .. file)
				os.execute(string.format("mpv --no-video '%s'", file))
			else
				print("\nInvalid selection.")
			end
		elseif choice == "2" then
			print("Exiting...")
			break
		else
			print("Invalid choice. Please try again.")
		end
	end
end

main()
