---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Centers for Environmental Information (NCEI / NOAA)
    url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-ecuador
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-ecuador
creator:
  affiliation: null
  email: null
  name: National Centers for Environmental Information (NCEI / NOAA)
  url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-ecuador
dataset_id: rdls_hzd-ecu_hdx_dailysummariesprecipitati_20151223
description: 'This dataset contains the daily summaries on base stations across Ecuador
  . The four indicators included are: * TPCP : Total precipitation * MXSD : Maximum
  snow depth * TSNW : Total snow fall * EMXP : Extreme maximum daily precipitation
  Indicators are compiled by the National Centers for Environmental Information (NCEI),
  which is administrated by National Oceanic and Atmospheric Administration (NOAA)
  an organization part of the United States government. NOAA has access to data collected
  from thousands of base stations around the world, which collect data periodically
  on weather and climate conditions. This dataset contains the latest 5 years of available
  data .. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-ecuador]'
details: Due to late-arriving data, the number of recent records is likely underrepresented
  in all categories, but the ratio of records (warm to cold, for example) should be
  a fairly strong estimate of a final outcome.
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
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC0-1.0
lineage:
  description: Daily precipitation indicators were compiled from thousands of base
    stations across Ecuador by NOAA's National Centers for Environmental Information.
    Stations were selected based on a minimum 30-year record requirement with at least
    182 complete days per year, ensuring consistent long-term meteorological observations
    suitable for drought and precipitation hazard characterization.
  sources:
  - id: source_1
    license: null
    name: National Centers for Environmental Information (NCEI / NOAA)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-ecuador
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
  url: https://www.ncdc.noaa.gov/cdo-web/datatools/records
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily Summaries of Precipitation Indicators for Ecuador (CSV)
  download_url: https://data.humdata.org/dataset/e37593d9-f4a1-4f59-b726-561324fcc106/resource/ac55a4d2-f7bd-45c5-ac75-86418d680983/download/precipitation_ecu.csv
  format: null
  id: resource_ac55a4d2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: precipitation_ecu.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ecu_hdx_dailysummariesprecipitati_20151223
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-23'
temporal_resolution: null
title: Daily Summaries of Precipitation Indicators for Ecuador
version: null
vulnerability: null
---
