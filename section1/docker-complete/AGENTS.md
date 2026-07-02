# AGENTS.md

# Vue.js Front-End Guidelines

## Philosophy

This project uses **Vue.js** as the framework while following a **React-friendly component architecture**.

The goal is to make every component easy to understand for engineers familiar with either Vue or React.

When multiple implementations are possible, choose the solution that provides:

* Explicit data flow
* Predictable state management
* High readability
* Easy debugging
* Reusable business logic
* Minimal framework-specific magic

Prefer simplicity over clever Vue-specific patterns.

Business logic should live outside of UI components whenever possible.

---

## Coding Convention

### 1. State Management

Use Vue Composition API consistently.

#### Rules

* Use `ref()` for primitive values.
* Use `reactive()` for objects and forms.
* Keep state local whenever possible.
* Avoid unnecessary global state.

#### Good

```ts
const count = ref(0);

const form = reactive({
  name: "",
  email: ""
});
```

#### Bad

```ts
const state = reactive({
  count: 0
});
```

when only a single primitive value is required.

---

### 2. Side Effects

Vue uses `watch()` instead of React's `useEffect`.

#### Rules

* Prefer `watch()` for dependency-based side effects.
* Use `watchEffect()` only when dependencies are obvious.
* Watch the minimum required value.
* Never watch an entire object if only one property is needed.

#### Good

```ts
watch(
    () => props.userId,
    loadUser
);
```

#### Bad

```ts
watch(props, loadUser);
```

---

### 3. Props

Treat props exactly like React props.

#### Rules

* Props are read-only.
* Never mutate props.
* If editable state is required, copy the value into a local `ref()`.

#### Good

```ts
const localName = ref(props.name);
```

#### Bad

```ts
props.name = "John";
```

---

### 4. Component Communication

Communication priority:

1. Props
2. Callback
3. Emit
4. Pinia (Global State)

#### Emit

Use `emit` only for simple UI notifications.

```ts
emit("close");
emit("select", item);
```

#### Callback

Use callbacks for business actions.

```ts
<UserForm
    :onSave="saveUser"
    :onDelete="deleteUser"
/>
```

Avoid long chains of `emit()` calls across multiple components.

Choose the approach that makes the execution flow easiest to follow.

---

### 5. Business Logic

UI components should remain lightweight.

Move reusable logic into composables.

#### Bad

```
Component
 ├── API
 ├── Validation
 ├── Business Logic
 └── UI
```

#### Good

```
Component
 └── UI

Composable
 ├── API
 ├── Validation
 ├── Business Logic
```

Components should primarily describe the UI.

---

### 6. Shared Libraries

Do not duplicate reusable code across projects.

Publish common modules as npm packages.

Examples:

```
@company/common-ui
@company/common-api
@company/common-utils
```

Preferred distribution:

* GitHub Packages
* GitLab Package Registry
* Private npm Registry

Projects should consume these packages as dependencies.

---

### 7. Code Review Checklist

Every Vue component should satisfy the following:

* State ownership is obvious.
* Props remain immutable.
* Watchers observe only necessary dependencies.
* Emit is used only for UI notifications.
* Business logic is extracted into composables.
* Common functionality belongs in shared packages.
* Component flow is understandable by React developers.

If there are multiple valid Vue implementations, prefer the one that is easiest to understand, maintain, and debug.
