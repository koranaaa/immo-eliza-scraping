def get_links(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.immoweb.be/en")

Handle cookie consent
    shadow_host = driver.find_element(By.ID, 'usercentrics-root')
    root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
    cookie_button = root.find_element(By.CSS_SELECTOR, '[data-testid=uc-accept-all-button]')
    cookie_button.click()

    # Search for properties
    driver.get(url)

Request page content
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract links to property listings
    links = [elem.get("href") for elem in soup.find_all("a", attrs={"class": "card__title-link"})]
    if not links:
        print("No properties found.")
        return None

    df = pd.DataFrame(links,columns=["Property Links"])
    df.to_csv('Links_immo.csv', index=False)

    print("Links saved to Links.csv")