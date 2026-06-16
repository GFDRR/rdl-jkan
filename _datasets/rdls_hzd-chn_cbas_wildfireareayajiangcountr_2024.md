---
attributions:
- entity:
    affiliation: null
    email: null
    name: SDGSAT-1 MSI (Multispectral Imager)
    url: https://data.humdata.org/dataset/the-wildfire-area-of-yajiang-country-sichuan-province-china
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Research Center of Big Data for Sustainable Development Goals
    (CBAS)
  url: https://data.humdata.org/dataset/the-wildfire-area-of-yajiang-country-sichuan-province-china
creator:
  affiliation: null
  email: null
  name: International Research Center of Big Data for Sustainable Development Goals
    (CBAS)
  url: https://data.humdata.org/dataset/the-wildfire-area-of-yajiang-country-sichuan-province-china
dataset_id: rdls_hzd-chn_cbas_wildfireareayajiangcountr_2024
description: 'This dataset contains SHP and TIFF. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/the-wildfire-area-of-yajiang-country-sichuan-province-china]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    wildfire:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Wildfire extent and area were delineated from SDGSAT-1 multispectral
    satellite imagery acquired on two dates in March 2024 covering Yajiang County,
    Sichuan Province. The burned area was calculated from the satellite observations
    and delivered as vector (SHP) and raster (TIFF) geospatial data products.
  sources:
  - id: source_1
    license: null
    name: SDGSAT-1 MSI (Multispectral Imager)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/the-wildfire-area-of-yajiang-country-sichuan-province-china
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The area of wildfires calculated in this SHP is based on SDGSAT-1 MSI
    images taken on 3 March 2024 and 19 March 2024. These burned areas in Yajiang
    County have an approximate area of 230 km2. TIS raster images of the areas affected
    by wildfires have also been uploaded.
  download_url: https://data.humdata.org/dataset/3d8047f8-599a-4aad-ab61-818c139daa5b/resource/c9d3efc4-f442-4c1d-bb92-4dc485d52ac3/download/yajiangwildfirearea.gdb.zip
  format: null
  id: resource_c9d3efc4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: YajiangWildfireArea.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-chn_cbas_wildfireareayajiangcountr_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - CHN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-05-19'
  start: '2024-03-03'
temporal_resolution: null
title: The wildfire area of Yajiang country, Sichuan Province, China
version: null
vulnerability: null
---
