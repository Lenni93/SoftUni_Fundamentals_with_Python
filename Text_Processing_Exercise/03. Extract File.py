file_name = input().split(".")

file = file_name[0].split("\\")
print(f"File name: {file[-1]}")
print(f"File extension: {file_name[1]}")


# C:\Internal\training-internal\Template.pptx
# File name: Template File extension: pptx#