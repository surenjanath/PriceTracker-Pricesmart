# Mobile App Security Guide

## ⚠️ CRITICAL: Never Hardcode API Keys

**Never** put your Supabase API keys directly in your mobile app code. Always use environment variables or configuration files.

## ✅ Safe Methods

### React Native / Expo

**✅ CORRECT - Use Environment Variables:**
```javascript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.EXPO_PUBLIC_SUPABASE_URL,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
);
```

**❌ WRONG - Hardcoded Keys:**
```javascript
// NEVER DO THIS!
const supabase = createClient(
  'https://your-project.supabase.co',
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' // ❌ EXPOSED KEY!
);
```

**Setup:**
1. Create `.env` file:
   ```
   EXPO_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
   EXPO_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
   ```

2. Add to `.gitignore`:
   ```
   .env
   .env.local
   ```

3. Install `react-native-dotenv` or use Expo's built-in env support

### Flutter

**✅ CORRECT - Use Environment Variables:**
```dart
import 'package:flutter_dotenv/flutter_dotenv.dart';

await dotenv.load(fileName: ".env");

await Supabase.initialize(
  url: dotenv.env['SUPABASE_URL']!,
  anonKey: dotenv.env['SUPABASE_ANON_KEY']!,
);
```

**❌ WRONG - Hardcoded Keys:**
```dart
// NEVER DO THIS!
await Supabase.initialize(
  url: 'https://your-project.supabase.co',
  anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...', // ❌ EXPOSED KEY!
);
```

**Setup:**
1. Add `flutter_dotenv` to `pubspec.yaml`:
   ```yaml
   dependencies:
     flutter_dotenv: ^5.0.2
   ```

2. Create `.env` file:
   ```
   SUPABASE_URL=https://your-project-id.supabase.co
   SUPABASE_ANON_KEY=your_anon_key_here
   ```

3. Add to `.gitignore`:
   ```
   .env
   ```

### iOS (Swift)

**✅ CORRECT - Use Info.plist:**
```swift
let supabaseURL = Bundle.main.object(forInfoDictionaryKey: "SUPABASE_URL") as! String
let supabaseKey = Bundle.main.object(forInfoDictionaryKey: "SUPABASE_ANON_KEY") as! String

let supabase = SupabaseClient(
  supabaseURL: URL(string: supabaseURL)!,
  supabaseKey: supabaseKey
)
```

**❌ WRONG - Hardcoded Keys:**
```swift
// NEVER DO THIS!
let supabase = SupabaseClient(
  supabaseURL: URL(string: "https://your-project.supabase.co")!,
  supabaseKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." // ❌ EXPOSED KEY!
)
```

**Setup:**
1. Add to `Info.plist`:
   ```xml
   <key>SUPABASE_URL</key>
   <string>https://your-project-id.supabase.co</string>
   <key>SUPABASE_ANON_KEY</key>
   <string>your_anon_key_here</string>
   ```

2. **Note**: For production, use environment-specific configs or secure keychain storage

### Android (Kotlin)

**✅ CORRECT - Use BuildConfig:**
```kotlin
val supabaseUrl = BuildConfig.SUPABASE_URL
val supabaseKey = BuildConfig.SUPABASE_ANON_KEY

val supabase = createSupabaseClient(
    supabaseUrl = supabaseUrl,
    supabaseKey = supabaseKey
) {
    install(Postgrest)
}
```

**❌ WRONG - Hardcoded Keys:**
```kotlin
// NEVER DO THIS!
val supabase = createSupabaseClient(
    supabaseUrl = "https://your-project.supabase.co",
    supabaseKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." // ❌ EXPOSED KEY!
) {
    install(Postgrest)
}
```

**Setup:**
1. Add to `local.properties` (add to `.gitignore`):
   ```properties
   SUPABASE_URL=https://your-project-id.supabase.co
   SUPABASE_ANON_KEY=your_anon_key_here
   ```

2. Add to `build.gradle`:
   ```gradle
   android {
       defaultConfig {
           buildConfigField "String", "SUPABASE_URL", "\"${project.findProperty("SUPABASE_URL")}\""
           buildConfigField "String", "SUPABASE_ANON_KEY", "\"${project.findProperty("SUPABASE_ANON_KEY")}\""
       }
   }
   ```

## 🔐 Security Best Practices

### ✅ DO:
- ✅ Use environment variables for all API keys
- ✅ Add `.env` / `local.properties` / config files to `.gitignore`
- ✅ Use **anon key** (public key) in mobile apps
- ✅ Use different keys for dev/staging/production
- ✅ Rotate keys periodically
- ✅ Use secure storage (Keychain/Keystore) for sensitive data

### ❌ DON'T:
- ❌ Hardcode API keys in source code
- ❌ Commit `.env` files to Git
- ❌ Use **service_role key** in mobile apps (server-side only!)
- ❌ Share keys in screenshots or documentation
- ❌ Store keys in version control
- ❌ Use the same key for all environments

## 📱 Which Key to Use?

### Mobile App (Client-Side)
- ✅ **anon key** (public key) - Safe for client-side use
- ❌ **service_role key** - NEVER use in mobile apps!

### Server-Side / CI/CD
- ✅ **service_role key** - Only for server-side scripts
- ✅ Use GitHub Secrets for CI/CD

## 🔍 How to Check if Keys Are Exposed

### Before Committing:
1. Search your codebase for:
   ```bash
   grep -r "eyJhbGci" .
   grep -r "service_role" .
   ```

2. Check `.gitignore` includes:
   ```
   .env
   .env.local
   local.properties
   *.keystore
   ```

3. Review all files being committed:
   ```bash
   git status
   git diff
   ```

### If Keys Are Exposed:
1. **Immediately** rotate the exposed keys in Supabase Dashboard
2. Remove keys from Git history (if already committed)
3. Update all apps/services using the old keys
4. Review access logs in Supabase

## 📚 Additional Resources

- [Supabase Security Best Practices](https://supabase.com/docs/guides/platform/security)
- [OWASP Mobile Security](https://owasp.org/www-project-mobile-security/)
- [React Native Security](https://reactnative.dev/docs/security)

## ✅ Checklist

Before deploying your mobile app:

- [ ] No hardcoded API keys in source code
- [ ] `.env` / config files in `.gitignore`
- [ ] Using anon key (not service_role)
- [ ] Environment variables properly loaded
- [ ] Different keys for dev/prod environments
- [ ] Keys rotated if previously exposed
- [ ] Code review completed
- [ ] Security scan passed

---

**Remember**: Once keys are committed to Git, they're in the history forever. Always use environment variables!

