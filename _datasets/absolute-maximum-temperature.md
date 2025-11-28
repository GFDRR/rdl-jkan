---
contact_point:
  email: briley@worldbank.org
  name: Bradley Riley
creator:
  email: briley@worldbank.org
  name: GFDRR
  url: https://www.gfdrr.org
dataset_id: rdls_hzd-T2M_max_ZAF
description: "Absolute maximum temperature. The baseline is calculated for 2001\u2013\
  2020, with projections for 2021\u20132040 and 2041\u20132060 under two climate scenarios:\
  \ RCP 4.5 (moderate emissions) and RCP 8.5 (high emissions)."
details: 'Heat stress indicators for present and future climates for the cities of
  Johannesburg and Ekurhuleni (South Africa) at 30m spatial resolution calculated
  with UrbClim (De Ridder et al., 2015) for the following scenarios: 2001-2020: present
  time (ERA5 input data), 2021-2040 RCP4.5 (CMIP5 ensemble), 2021-2040 RCP8.5 (CMIP5
  ensemble), 2041-2060 RCP4.5 (CMIP5 ensemble), and  2041-2060 RCP8.5 (CMIP5 ensemble)'
exposure: null
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: extreme_temperature
  intensity: WBGT:c
  occurrence_range: ''
  processes: extreme_heat
license: CC-BY-4.0
loss: null
project: Future Heat Stress Indicators for Johannesburg and Ekurhuleni
publisher:
  email: njones@worldbankgroup.org; niels.souverijns@vito.be
  name: GFDRR; VITO
  url: https://www.gfdrr.org; https://vito.be
purpose: 'This dataset is part of the scientific paper: Souverijns, N., De Ridder,
  K., Veldeman, N., Lefebre, F., Kusambiza-Kiingi, F., Memela, W., Jones, N.K.W.,
  2022. Urban heat in Johannesburg and Ekurhuleni, South Africa: A meter-scale assessment
  and vulnerability analysis. Urban Climate, 46, 101331. https://doi.org/10.1016/j.uclim.2022.101341'
resources:
- coordinate_system: EPSG:4326
  description: Absolute maximum temperature for the period 2001-2020.
  download_url: https://zenodo.org/records/6394130
  format: geotiff
  id: '0'
  spatial_resolution: null
  title: Absolute Maximum Temperature - Johannebsurg & Ekurhuleni (2001-2020)
- coordinate_system: EPSG:4326
  description: Projected absolute maximum temperature under the RCP 4.5 and 8.5 scenario
    for 2021-2040.
  download_url: https://zenodo.org/records/6394130
  format: geotiff
  id: '1'
  spatial_resolution: null
  title: Absolute Maximum Temperature - Johannebsurg & Ekurhuleni (2021-2040, RCP4.5
    & RCP8.5)
- coordinate_system: EPSG:4326
  description: Projected absolute maximum temperature under the RCP 4.5 and 8.5 scenario
    for 2041-2060.
  download_url: https://zenodo.org/records/6394130
  format: geotiff
  id: '2'
  spatial_resolution: null
  title: Absolute Maximum Temperature - Johannebsurg & Ekurhuleni (2041-2060, RCP4.5
    & RCP8.5)
risk_data_type:
- hazard
schema: rdl-02
slug: rdls_hzd-T2M_max_ZAF
spatial:
  bbox:
  - 27.676831894273278
  - -26.580113703331147
  - 28.588018624040238
  - -25.838677579993774
  centroid:
  - 28.132425259156758
  - -26.20939564166246
  countries:
  - ZAF
  gazetteer_entries:
  - description: City of Johannesburg, Gauteng Province
    id: ZAF-GP-JHB
    scheme: ISO 3166-2
  - description: City of Ekurhuleni, Gauteng Province
    id: ZAF-GP-EKU
    scheme: ISO 3166-2
  scale: sub-national
title: Absolute Maximum Temperature
version: 30 March 2022
vulnerability: null
---
