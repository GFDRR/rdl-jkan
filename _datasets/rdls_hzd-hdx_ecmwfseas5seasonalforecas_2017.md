---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Centre for Medium-Range Weather Forecasts (ECMWF) SEAS5
    url: https://data.humdata.org/dataset/ecmwf-anomalous-precipitation
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Copernicus Climate Data Store
    url: https://data.humdata.org/dataset/ecmwf-anomalous-precipitation
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/ecmwf-anomalous-precipitation
creator:
  affiliation: null
  email: null
  name: Copernicus Climate Data Store
  url: https://data.humdata.org/dataset/ecmwf-anomalous-precipitation
dataset_id: rdls_hzd-hdx_ecmwfseas5seasonalforecas_2017
description: 'This data can be used to identify how forecasted precipitation may differ
  from the long term average, for a given location and time of the year. These anomalies
  are calculated by the European Centre for Medium-Range Weather Forecasts (ECMWF)
  and are based on their SEAS5 seasonal precipitation forecast. SEAS5 is an ensemble
  forecast, meaning that the weather model outputs many possible scenarios, leading
  to probabilistic outcomes. The data presented here is the result of averaging all
  outputs (the ''ensemble mean''). Additional postprocessing has been applied here
  to aggregate ECMWF''s gridded outputs across administrative boundaries (at both
  admin 0 and admin 1 levels). The gridded product can also be accessed from the Copernicus
  Climate Data Store (CDS) . Data is available on the 5th of each month, with up to
  6 months of lead time (including the current month). Anomaly values are in mm/month,
  with positive values indicating above average precipitation. The resources in this
  dataset include: Full admin 0 historical record of anomalies (forecast_precipitation_anomalies_adm0.csv)
  Recent admin 1 global anomalies (forecast_precipitation_anomalies_adm1_global_3yrs.csv)
  Full admin 1 historical record of anomalies, separated by region (forecast_precipitation_anomalies_adm1_{region}.csv)
  Geotiffs of anomalies based on latest forecast (forecast_precipitation_anomalies_geotiff_{forecast_date}.zip).
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ecmwf-anomalous-precipitation]'
details: The gridded product from ECMWF is provided at a 1 degree resolution. Forecast
  skill is variable, particularly across longer lead times. Forecast skill may also
  vary significantly by location, with even a negative correlation in some locations
  and lead times. See [these plots](https://confluence.ecmwf.int/display/CKB/C3S+seasonal+forecasts+verification+plots)
  from ECMWF for more information. Users should be careful in their handling of the
  temporal attributes of this dataset. Variables prefixed with 'issue_' refer to the
  time that the forecast was issued by ECMWF. Variables prefixed with 'valid_' refer
  to the time that the forecast applies to. The difference in months between 'issued_'
  and 'valid_' dates is captured by the 'lead_time' variable.
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: probabilistic
      calculation_method: simulated
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
  description: ECMWF SEAS5 ensemble seasonal precipitation forecasts are post-processed
    by calculating anomalies relative to a 1993-2016 climatological baseline. Monthly
    anomalous precipitation rates are aggregated to total accumulated precipitation
    per month in millimeters and spatially aggregated to administrative boundaries
    (ADM0, ADM1) and gridded formats (GeoTIFF) for global distribution.
  sources:
  - id: source_1
    license: null
    name: European Centre for Medium-Range Weather Forecasts (ECMWF) SEAS5
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Copernicus Climate Data Store
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ecmwf-anomalous-precipitation
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
  url: https://ecmwf-projects.github.io/copernicus-training-c3s/sf-anomalies.html
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summarized forecast precipitation anomalies data at adm0 from 2017-01-01
    to 2025-12-31
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/02cd7aee-d303-407e-a486-74edb5571daa/download/forecast_precipitation_anomalies_adm0.csv
  format: null
  id: resource_02cd7aee
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_adm0.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summarized forecast precipitation anomalies data at adm1 from 2017-01-01
    to 2025-12-31
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/293ec6d0-2729-4bd5-a4fd-40a30faf1052/download/forecast_precipitation_anomalies_adm1_global_3yrs.csv
  format: null
  id: resource_293ec6d0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_adm1_global_3yrs.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summarized forecast precipitation anomalies data at adm1 from 2017-01-01
    to 2025-12-31 for Asia
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/929d9800-0dbd-4612-92b2-447873f91a39/download/forecast_precipitation_anomalies_adm1_asia.csv
  format: null
  id: resource_929d9800
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_adm1_asia.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summarized forecast precipitation anomalies data at adm1 from 2017-01-01
    to 2025-12-31 for Africa
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/6d9fa931-b9c5-4cc6-a6d3-7c7f9a087de2/download/forecast_precipitation_anomalies_adm1_africa.csv
  format: null
  id: resource_6d9fa931
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_adm1_africa.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summarized forecast precipitation anomalies data at adm1 from 2017-01-01
    to 2025-12-31 for Americas
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/9e2d58bc-ba78-47e7-ab11-76cf7d709e1c/download/forecast_precipitation_anomalies_adm1_americas.csv
  format: null
  id: resource_9e2d58bc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_adm1_americas.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summarized forecast precipitation anomalies data at adm1 from 2017-01-01
    to 2025-12-31 for Europe
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/f3cebb44-60c1-4422-be8b-474aee65318e/download/forecast_precipitation_anomalies_adm1_europe.csv
  format: null
  id: resource_f3cebb44
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_adm1_europe.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summarized forecast precipitation anomalies data at adm1 from 2017-01-01
    to 2025-12-31 for Oceania
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/b4a20c53-03ed-4752-aab6-fad362c76148/download/forecast_precipitation_anomalies_adm1_oceania.csv
  format: null
  id: resource_b4a20c53
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_adm1_oceania.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: ECMWF SEAS5 Seasonal Forecasts - Anomalous Precipitation (Latest forecast
    precipitation anomalies raster data from 2025-12)
  download_url: https://data.humdata.org/dataset/a0e34f02-6d1d-4160-9e0a-f93a19a1f2e8/resource/77392ed5-8f41-4ac9-a5a0-58d00221a688/download/forecast_precipitation_anomalies_geotiff_2025_12.zip
  format: null
  id: resource_77392ed5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: forecast_precipitation_anomalies_geotiff_2025_12.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hdx_ecmwfseas5seasonalforecas_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: ECMWF SEAS5 Seasonal Forecasts - Anomalous Precipitation
version: null
vulnerability: null
---
