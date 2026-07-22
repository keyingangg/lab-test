const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const { expect } = require('chai');

describe('Login page', function () {
  let driver;

  before(async function () {
    const options = new chrome.Options();
    options.addArguments('--headless=new', '--no-sandbox', '--disable-dev-shm-usage');
    driver = await new Builder()
      .forBrowser('chrome')
      .setChromeOptions(options)
      .build();
  });

  after(async function () {
    if (driver) await driver.quit();
  });

  it('loads and input works', async function () {
    await driver.get('http://localhost:5000');

    // Check page loaded
    await driver.wait(until.titleMatches(/Login/i), 5000);

    // Type a password
    const passwordInput = await driver.findElement(By.name('password'));
    await passwordInput.sendKeys('SUPERsecurepass31231!@#');

    // Click login
    await driver.findElement(By.css('button[type="submit"]')).click();

    // Verify redirect
    await driver.wait(until.urlMatches(/login/), 5000);

    // Check password is displayed
    const bodyText = await driver.findElement(By.css('body')).getText();
    expect(bodyText).to.include('SUPERsecurepass31231!@#');
  });
});
