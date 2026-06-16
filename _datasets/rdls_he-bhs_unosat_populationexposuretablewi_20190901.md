---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/population-exposure-table-by-windspeed-zone-at-district-level-in-bahamas
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-exposure-table-by-windspeed-zone-at-district-level-in-bahamas
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-exposure-table-by-windspeed-zone-at-district-level-in-bahamas
dataset_id: rdls_he-bhs_unosat_populationexposuretablewi_20190901
description: 'Pivot table summarizing total population potentially exposed to strong
  winds. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-exposure-table-by-windspeed-zone-at-district-level-in-bahamas]'
details: null
exposure:
- asset_type:
    description: Population exposed to strong wind hazard zones at district level
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT processed satellite data and operational cyclone information
    to delineate wind speed zones across Bahamas districts, then intersected with
    population distribution data using GIS to generate exposure pivot tables summarizing
    population counts by wind hazard intensity zone.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-exposure-table-by-windspeed-zone-at-district-level-in-bahamas
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
  description: Population exposure table by windspeed zone at district level in Bahamas
    (Population exposure to wind speed zones table by district in Bahamas)
  download_url: https://data.humdata.org/dataset/3810410c-9069-4795-8bf3-c74d6707279c/resource/17f1bcdf-9dd0-47bc-9ad2-fcac174fd68c/download/unosat_tropicalcyclone_dorian_population_exposure_analysis.xlsx
  format: null
  id: resource_17f1bcdf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_TropicalCyclone_Dorian_Population_Exposure_Analysis.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bhs_unosat_populationexposuretablewi_20190901
spatial:
  bbox: null
  centroid: null
  countries:
  - BHS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-09-01'
temporal_resolution: null
title: Population exposure table by windspeed zone at district level in Bahamas
version: null
vulnerability: null
---
