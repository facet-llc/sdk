// Release guard: package.json `version` and the newest dated changelog
// section must move together. A version bump without its matching
// `## [X.Y.Z] - YYYY-MM-DD` heading (or a dated heading without the bump)
// fails here, so a release can never ship with a stale changelog.

import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";

const packageJson = JSON.parse(
  readFileSync(new URL("../package.json", import.meta.url), "utf8"),
) as { version: string };

const changelog = readFileSync(new URL("../CHANGELOG.md", import.meta.url), "utf8");

describe("package version matches the newest dated changelog section", () => {
  it("package.json version equals the top-most `## [X.Y.Z] - YYYY-MM-DD` heading", () => {
    const match = changelog.match(/^## \[(\d+\.\d+\.\d+)\] - \d{4}-\d{2}-\d{2}/m);
    expect(match).not.toBeNull();
    const changelogVersion = match![1];
    expect(changelogVersion).toBeDefined();
    expect(packageJson.version).toBe(changelogVersion!);
  });
});
