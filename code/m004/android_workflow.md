

I'll create a workflow guide for developing and testing the Flutter app using the Android emulator.

```markdown:code/m004/android_workflow.md
# Android Development Workflow Guide

## 1. Setup Environment

### Install Required Tools
```bash
# Check if you have Java installed
java -version

# Install Android Studio
# Download from: https://developer.android.com/studio

# Install Flutter
# Download from: https://flutter.dev/docs/get-started/install

# Verify installation
flutter doctor
```

## 2. Configure Android Studio

1. Open Android Studio
2. Go to Settings/Preferences
3. Install plugins:
   - Flutter
   - Dart

## 3. Create Android Virtual Device (AVD)

1. In Android Studio:
   - Tools > Device Manager
   - Click "Create Device"
   - Select phone model (e.g., Pixel 4)
   - Download and select system image (recommend API 33)
   - Name your AVD and click Finish

## 4. Project Setup

```bash
# Create new Flutter project
flutter create question_app
cd question_app

# Get dependencies
flutter pub get
```

## 5. Development Workflow

### Start the Emulator
```bash
# List available emulators
flutter emulators

# Start emulator (replace emulator_id with your AVD name)
flutter emulators --launch <emulator_id>

# Alternative: Start from Android Studio
# Tools > Device Manager > Play button next to your AVD
```

### Run the App
```bash
# Run app in debug mode
flutter run

# Build release version
flutter build apk
```

## 6. Testing Commands

```bash
# Hot reload (while app is running)
r

# Hot restart
R

# Quit
q

# Check connected devices
flutter devices
```

## 7. Debugging Tips

- Use print() statements for console logging
- Enable Debug Paint: Press 'p' in terminal while running
- Enable Performance Overlay: Press 'P' in terminal
- Android Studio debugger: Set breakpoints and use Debug mode

## 8. Common Issues & Solutions

### If emulator is slow:
1. Enable Hardware Acceleration in BIOS
2. Increase RAM allocation in AVD settings
3. Use a lower API level emulator

### If app won't start:
```bash
# Clean and rebuild
flutter clean
flutter pub get
flutter run
```

### If Flutter doctor shows issues:
```bash
flutter doctor --android-licenses
```

## 9. Building for Release

```bash
# Generate keystore
keytool -genkey -v -keystore ~/key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias key

# Build release APK
flutter build apk --release

# Build app bundle
flutter build appbundle
```

## 10. Testing Checklist

- [ ] App launches successfully
- [ ] All buttons respond to clicks
- [ ] Text is readable on different screen sizes
- [ ] Answers are recorded correctly
- [ ] UI elements are properly aligned
- [ ] No overflow errors
- [ ] Back button behavior works
- [ ] App state persists as expected

## 11. Performance Testing

```bash
# Run performance analysis
flutter run --profile

# Generate performance metrics
flutter run --trace-startup
```

Remember to test on multiple screen sizes and Android versions for best results.
```

This workflow guide provides a structured approach to developing and testing your Flutter app using the Android emulator. Let me know if you need more detailed information about any specific step!
