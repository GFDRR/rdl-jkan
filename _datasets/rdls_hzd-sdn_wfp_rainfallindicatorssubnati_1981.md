---
attributions:
- entity:
    affiliation: null
    email: null
    name: Climate Hazards Group InfraRed Precipitation with Stations (CHIRPS) version
      2
    url: https://data.humdata.org/dataset/sdn-rainfall-subnational
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CHIRPS-GEFS short term rainfall forecasts
    url: https://data.humdata.org/dataset/sdn-rainfall-subnational
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/sdn-rainfall-subnational
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/sdn-rainfall-subnational
dataset_id: rdls_hzd-sdn_wfp_rainfallindicatorssubnati_1981
description: 'This dataset contains dekadal rainfall indicators, computed from Climate
  Hazards Group InfraRed Precipitation satellite imagery with insitu Station data
  (CHIRPS) version 2 and the CHIRPS-GEFS short term rainfall forecasts, aggregated
  by subnational administrative units. Included indicators are (for each dekad): 10
  day rainfall [mm] ( rfh ) rainfall 1-month rolling aggregation [mm] ( r1h ) rainfall
  3-month rolling aggregation [mm] ( r3h ) rainfall long term average [mm] ( rfh_avg
  ) rainfall 1-month rolling aggregation long term average [mm] ( r1h_avg ) rainfall
  3-month rolling aggregation long term average [mm] ( r3h_avg ) rainfall anomaly
  [%] ( rfq ) rainfall 1-month anomaly [%] ( r1q ) rainfall 3-month anomaly [%] (
  r3q ) The administrative units used for aggregation are based on WFP data and contain
  a Pcode reference attributed to each unit. The number of input pixels used to create
  the aggregates, is provided in the n_pixels column. Finally, the type column indicates
  if the value is based on a forecast, a preliminary or a final product. Forecasts
  are issued on the 6th, 16th, and 26th of each month for the upcoming 10-day period
  (dekad), then updated with improved versions on the 1st, 11th, and 21st. Preliminary
  observations replace the previous dekad''s forecast on the 3rd, 13th, and 23rd,
  and are later replaced by final observations-published mid-month (13th or 23rd)-covering
  all three dekads of the prior month. Please find a summary below: Publication Day:
  Forecast type, Covers (Dekad) 1st: Updated forecast, 1-10 of the same month 6th:
  Initial forecast, 11-20 of the same month 11th: Updated forecast, 1-10 of the same
  month 16th: Initial forecast, 21-end of the same month 21st: Updated forecast, 11-20
  of the same month 26th: Initial forecast, 1-10 of the following month For more on
  CHIRPS-GEFS forecasts, see: https://www.chc.ucsb.edu/data/chirps-gefs For further
  details, please see the methodology section.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/sdn-rainfall-subnational]'
details: To provide real-time data, the prelim version is used which then gets replaced
  successively by final data as it becomes available. For more information about differences
  between prelim and final see [CHIRPS Reality Checks](https://wiki.chc.ucsb.edu/CHIRPS_Reality_Checks).
  Forecast data is successively replaced by preliminary and final data.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SMA:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Dekadal rainfall data derived from CHIRPS satellite imagery merged
    with station observations, aggregated to subnational administrative units. Rolling
    1-month and 3-month aggregations computed alongside long-term climatological averages
    to generate drought indicators (rainfall quantiles and anomalies) for monitoring
    meteorological drought conditions.
  sources:
  - id: source_1
    license: null
    name: Climate Hazards Group InfraRed Precipitation with Stations (CHIRPS) version
      2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: CHIRPS-GEFS short term rainfall forecasts
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sdn-rainfall-subnational
  rel: source
loss: null
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
  url: https://chc.ucsb.edu/data/chirps
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://chc.ucsb.edu/data/chirps-gefs
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This resource contains the full timeseries to date. File id: 20260123T135545723369_f1888efc'
  download_url: https://data.humdata.org/dataset/139b7e9c-3c40-49e0-a44e-0eed6dad46d2/resource/e30c357b-05c3-44f1-97f1-1775726ce57c/download/sdn-rainfall-subnat-full.csv
  format: null
  id: resource_e30c357b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn-rainfall-subnat-full.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This resource contains a subset of the full timeseries covering the
    past five years to date. File id: 20260123T135545723369_f1888efc'
  download_url: https://data.humdata.org/dataset/139b7e9c-3c40-49e0-a44e-0eed6dad46d2/resource/9359abcf-d1fc-41dd-b2a5-f27278e87bd7/download/sdn-rainfall-subnat-5ytd.csv
  format: null
  id: resource_9359abcf
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn-rainfall-subnat-5ytd.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_wfp_rainfallindicatorssubnati_1981
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '1981-01-01'
temporal_resolution: null
title: 'Sudan: Rainfall Indicators at Subnational Level'
version: null
vulnerability: null
---
