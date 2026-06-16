---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/somalia-flooding-jilib-saakow-and-bu-aale-districs-2018-05-01
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Field Information Services Section (FISS)
  url: https://data.humdata.org/dataset/somalia-flooding-jilib-saakow-and-bu-aale-districs-2018-05-01
creator:
  affiliation: null
  email: null
  name: OCHA Field Information Services Section (FISS)
  url: https://data.humdata.org/dataset/somalia-flooding-jilib-saakow-and-bu-aale-districs-2018-05-01
dataset_id: rdls_he-som_ochafiss_floodingjilibsaakowbuaale_20180503
description: 'UNOSAT produced satellite-detected flood water extent in the districts
  of Jilib, Saakow, and Bu''aale, Somalia. The analysis was conducted analyzing Sentinel-1
  images acquired on the 1 May 2018. As observed from the satellite imagery, a total
  of 92,000 ha of land were inundated in the area of interest. The most affected districts
  are Saakow, with almost 38,000 ha of flooded land and southern Diinsoor, with almost
  27,000 ha. At least 20 settlements are potentially located within the flooded area.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-flooding-jilib-saakow-and-bu-aale-districs-2018-05-01]'
details: 'From UNOSAT documentation: ''It is likely that flood waters have been systematically
  underestimated along highly vegetated areas along main river banks and within built-up
  urban areas because of the special characteristics of the satellite data used. '''
exposure:
- asset_type:
    description: Land area inundated by floodwaters, totaling 92,000 hectares across
      the three districts
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: At least 20 settlements potentially located within the flooded area
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analyzed Sentinel-1 SAR imagery acquired on 1 May 2018 to detect
    and map flood water extent across three districts in Middle Juba region, Somalia.
    Water classification was performed on the satellite imagery with confidence assessments
    and field validation notes recorded. Pre-flood baseline imagery from 29 December
    2014 was also provided for comparison.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-flooding-jilib-saakow-and-bu-aale-districs-2018-05-01
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia flooding Jilib, Saakow, and Bu'aale districts 2018 05 01 (2018
    05 01 flooding - Jilib, Saakow, and Bu'aale districts, Somalia)
  download_url: https://data.humdata.org/dataset/2c8b44ba-38a4-4f72-895e-814e590195f6/resource/25392bb3-0522-42b8-a863-a3508c933a54/download/st20180501_middle_juba_flood_water.zip
  format: null
  id: resource_25392bb3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ST20180501_Middle_Juba_Flood_Water.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia flooding Jilib, Saakow, and Bu'aale districts 2018 05 01 (Pre-flooding
    - Jilib, Saakow, and Bu'aale districts, Somalia)
  download_url: https://data.humdata.org/dataset/2c8b44ba-38a4-4f72-895e-814e590195f6/resource/71f098eb-262e-4c64-8c39-e629495b7509/download/st20141229_preflood.zip
  format: null
  id: resource_71f098eb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ST20141229_PreFlood.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_ochafiss_floodingjilibsaakowbuaale_20180503
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-03'
temporal_resolution: null
title: Somalia flooding Jilib, Saakow, and Bu'aale districts 2018 05 01
version: null
vulnerability: null
---
