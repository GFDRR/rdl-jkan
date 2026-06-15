---
attributions:
- entity:
    affiliation: null
    email: null
    name: CHIRPS v2.0
    url: https://data.humdata.org/dataset/east-africa-chirps-seasonal-rainfall-accumulation-anomaly-by-pentad
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: USGS
    url: https://data.humdata.org/dataset/east-africa-chirps-seasonal-rainfall-accumulation-anomaly-by-pentad
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FEWS NET
    url: https://data.humdata.org/dataset/east-africa-chirps-seasonal-rainfall-accumulation-anomaly-by-pentad
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/east-africa-chirps-seasonal-rainfall-accumulation-anomaly-by-pentad
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/east-africa-chirps-seasonal-rainfall-accumulation-anomaly-by-pentad
dataset_id: rdls_hzd-ethkensomtzauga_hdx_eastafricachirpsseasonalr_2023
description: "Climate Hazards Group InfraRed Precipitation with Station data (CHIRPS)\
  \ is a 35+ year quasi-global rainfall data set. It is a gridded rainfall time series\
  \ for trend analysis and seasonal drought monitoring, spans 50\xB0S-50\xB0N (and\
  \ all longitudes) and ranges from 1981 to near-present. The anomaly refers to the\
  \ difference between current rainfall and the average rainfall that occurred between\
  \ 1981 and 2010 in millimeters. For more information visit the CHIRPS site . This\
  \ dataset contains the latest available CHIRPS anomaly data. The full list of data\
  \ available is available from USGS for Mar-May data , Oct-Dec data , and others.\
  \ Additionally, subnational statistics (mean, min, max) have been calculated for\
  \ Ethiopia, Kenya, and Somalia and are available in the csv resource.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/east-africa-chirps-seasonal-rainfall-accumulation-anomaly-by-pentad]"
details: null
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
        intensity_measure: SMA:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: CHIRPS v2.0 gridded precipitation observations are accumulated by pentad
    over seasonal periods (October-December, March-May). Seasonal cumulative rainfall
    anomalies are computed as the difference between current season totals and the
    1981-2010 climatological average. Results are provided as GeoTIFF rasters and
    subnational summary statistics for East African drought monitoring.
  sources:
  - id: source_1
    license: null
    name: CHIRPS v2.0
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: USGS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: FEWS NET
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/east-africa-chirps-seasonal-rainfall-accumulation-anomaly-by-pentad
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
  url: https://earlywarning.usgs.gov/fews/product/598
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Latest anomaly data summarized by subnational admin unit for Ethiopia,
    Kenya, and Somalia.
  download_url: https://data.humdata.org/dataset/bfedda6e-4902-4cd8-9b05-410d00e70660/resource/a3524f32-7fd7-46d4-9061-94d24585de18/download/subnational_anomaly_statistics.csv
  format: null
  id: resource_a3524f32
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: subnational_anomaly_statistics.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'October to December 2023 (Oct pentad 1 thru Dec Pentad 6) - Average(1981-2010)
    Pentad: 72'
  download_url: https://edcintl.cr.usgs.gov/downloads/sciweb1/shared/fews/web/africa/east/pentadal/chirps/seasaccum/octdec/anom/lta/downloads/pentadal/ea_chirps_seasaccum_anom_octdec_202372_lta.zip
  format: null
  id: resource_de017ef5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ea_chirps_seasaccum_anom_octdec_202372_lta
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'March to May 2024 (Mar pentad 1 thru May Pentad 6) - Average(1981-2010)
    Pentad: 30'
  download_url: https://edcintl.cr.usgs.gov/downloads/sciweb1/shared/fews/web/africa/east/pentadal/chirps/seasaccum/marmay/anom/lta/downloads/pentadal/ea_chirps_seasaccum_anom_marmay_202430_lta.zip
  format: null
  id: resource_97677940
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ea_chirps_seasaccum_anom_marmay_202430_lta
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ethkensomtzauga_hdx_eastafricachirpsseasonalr_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  - KEN
  - SOM
  - TZA
  - UGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-05-31'
  start: '2023-12-26'
temporal_resolution: null
title: East Africa - CHIRPS Seasonal Rainfall Accumulation Anomaly by Pentad
version: null
vulnerability: null
---
