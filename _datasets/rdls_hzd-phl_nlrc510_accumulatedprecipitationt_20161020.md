---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA Global Precipitation Measurement (GPM)
    url: https://data.humdata.org/dataset/philippines-accumulated-precipitation-typhoon-haima-11-20th-october-2016-zip
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-accumulated-precipitation-typhoon-haima-11-20th-october-2016-zip
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-accumulated-precipitation-typhoon-haima-11-20th-october-2016-zip
dataset_id: rdls_hzd-phl_nlrc510_accumulatedprecipitationt_20161020
description: 'This data is created using GPM data. It contains the accumulated precipitation
  for the periods October 11-18th, October 18-20th and the total over both periods..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-accumulated-precipitation-typhoon-haima-11-20th-october-2016-zip]'
details: This data has been sourced from GPM (https://pmm.nasa.gov/data-access/downloads/gpm)
exposure: []
hazard:
  event_sets_by_hazard_type:
    convective_storm:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: RF:mm
        process: thunderstorm
        trigger: null
        type: convective_storm
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Accumulated precipitation data was derived from NASA's Global Precipitation\
    \ Measurement (GPM) satellite observations during Typhoon Haima's passage over\
    \ the Philippines (October 11\u201320, 2016). The data was processed by Netherlands\
    \ Red Cross 510 to produce accumulated rainfall totals for two sub-periods (October\
    \ 11\u201318 and October 18\u201320) and a combined total, distributed as shapefiles\
    \ and CSV for disaster response and impact assessment purposes."
  sources:
  - id: source_1
    license: null
    name: NASA Global Precipitation Measurement (GPM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-accumulated-precipitation-typhoon-haima-11-20th-october-2016-zip
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
  description: Philippines - Accumulated precipitation, Typhoon Haima - 11-20th October
    2016.zip
  download_url: https://data.humdata.org/dataset/068b4285-70a1-4dcd-8bcd-432183ad9c0d/resource/e68faefe-e37a-4ec0-bf1f-1664cf73ee5a/download/typhoon_haima_rainfall_per_municipality_1.zip
  format: null
  id: resource_e68faefe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Philippines - Accumulated precipitation, Typhoon Haima - 11-20th October
    2016.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Accumulated precipitation, Typhoon Haima - 11-20th October
    2016 (Data for 11-20th, 18-20th are available)
  download_url: https://data.humdata.org/dataset/068b4285-70a1-4dcd-8bcd-432183ad9c0d/resource/53912537-62bb-4e96-9e08-4aeedf2f5ab4/download/typhoon_haima_accumulated_rainfall.csv
  format: null
  id: resource_53912537
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Philippines - Accumulated precipitation, Typhoon Haima - 11-20th October
    2016.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_nlrc510_accumulatedprecipitationt_20161020
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-20'
temporal_resolution: null
title: Philippines - Accumulated precipitation, Typhoon Haima - 11-20th October 2016
version: null
vulnerability: null
---
