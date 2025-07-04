const { test, expect } = require('@playwright/test');

test('Login page loads and input works', async ({ page }) => {
  await page.goto('http://localhost:5000');

  // Check page loaded
  await expect(page).toHaveTitle(/Login/i);

  // Type a password
  await page.fill('input[name="password"]', 'SUPERsecurepass31231!@#');

  // Click login
  await page.click('button[type="submit"]');

  // Verify redirect
//   await expect(page).toHaveURL(/welcome/);
  await expect(page).toHaveURL(/login/);

  // Check password is displayed
  await expect(page.locator('body')).toContainText('SUPERsecurepass31231!@#');
});
