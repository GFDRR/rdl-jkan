---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA Moderate Resolution Imaging Spectroradiometer (MODIS)
    url: https://data.humdata.org/dataset/gmb-ndvi-subnational
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP
    url: https://data.humdata.org/dataset/gmb-ndvi-subnational
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/gmb-ndvi-subnational
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/gmb-ndvi-subnational
dataset_id: rdls_hzd-gmb_wfp_ndvisubnationallevel_2002
description: 'This dataset contains dekadal NDVI indicators computed from NASA''s
  Moderate Resolution Imaging Spectroradiometer (MODIS) collection 6.1 from the Aqua
  and Terra satellite aggregated by sub-national administrative units. Included indicators
  are (for each dekad): 10 day NDVI ( vim ) NDVI long term average ( vim_lta ) 10
  day NDVI anomaly [%] ( viq ) The administrative units used for aggregation are based
  on WFP data and contain a Pcode reference attributed to each unit. The number of
  input pixels used to create the aggregates, is provided in the n_pixels column..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/gmb-ndvi-subnational]'
details: Due to the nature of the Whittaker filter, the update of the timeseries (i.e.
  the addition of a new dekad) has an effect of preceding dekads which diminishes
  going back in time. Therefore slight variations can be expected for a certain number
  of dekads for every update.
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: NDVI:-
        process: agricultural_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Raw MODIS AQUA and TERRA 16-day composite products (MYD13C1 and MOD13C1)
    were integrated into 8-day synthetic products and processed to compute dekadal
    NDVI values. NDVI indicators (10-day index, long-term average, and percentage
    anomaly) were aggregated by WFP-defined sub-national administrative units with
    Pcode references to create time-series vegetation monitoring data for drought
    assessment.
  sources:
  - id: source_1
    license: null
    name: NASA Moderate Resolution Imaging Spectroradiometer (MODIS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WFP
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gmb-ndvi-subnational
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://lpdaac.usgs.gov/products/myd13c1v061/
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://lpdaac.usgs.gov/products/mod13c1v061/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This resource contains the full timeseries to date. File id: 20260123T135523724244_b603b576'
  download_url: https://data.humdata.org/dataset/4cf439c8-bd14-4fcc-9579-b3ca729ae59f/resource/dd32ffcc-c224-4a8c-b248-5acefb9e9dad/download/gmb-ndvi-subnat-full.csv
  format: null
  id: resource_dd32ffcc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gmb-ndvi-subnat-full.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This resource contains a subset of the full timeseries covering the
    past five years to date. File id: 20260123T135523724244_b603b576'
  download_url: https://data.humdata.org/dataset/4cf439c8-bd14-4fcc-9579-b3ca729ae59f/resource/8ddb7c3c-0e1c-4de8-9cee-3dd28e3501a7/download/gmb-ndvi-subnat-5ytd.csv
  format: null
  id: resource_8ddb7c3c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gmb-ndvi-subnat-5ytd.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gmb_wfp_ndvisubnationallevel_2002
spatial:
  bbox: null
  centroid: null
  countries:
  - GMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-20'
  start: '2002-07-01'
temporal_resolution: null
title: 'Gambia: NDVI at Subnational Level'
version: null
vulnerability: null
---
