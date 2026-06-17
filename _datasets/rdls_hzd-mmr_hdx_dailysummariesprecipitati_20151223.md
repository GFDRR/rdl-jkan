---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Centers for Environmental Information (NCEI / NOAA)
    url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-myanmar
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-myanmar
creator:
  affiliation: null
  email: null
  name: National Centers for Environmental Information (NCEI / NOAA)
  url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-myanmar
dataset_id: rdls_hzd-mmr_hdx_dailysummariesprecipitati_20151223
description: 'This dataset contains the daily summaries on base stations across Myanmar
  . The four indicators included are: * TPCP : Total precipitation * MXSD : Maximum
  snow depth * TSNW : Total snow fall * EMXP : Extreme maximum daily precipitation
  Indicators are compiled by the National Centers for Environmental Information (NCEI),
  which is administrated by National Oceanic and Atmospheric Administration (NOAA)
  an organization part of the United States government. NOAA has access to data collected
  from thousands of base stations around the world, which collect data periodically
  on weather and climate conditions. This dataset contains the latest 5 years of available
  data .. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-myanmar]'
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
  type: drought
license: CC0-1.0
lineage:
  description: Daily precipitation and snow measurements were collected from meteorological
    base stations across Myanmar by NOAA's National Centers for Environmental Information.
    Stations were selected based on a minimum 30-year record requirement with at least
    182 complete days per year. Data were compiled and quality-controlled to produce
    daily summaries of total precipitation, maximum snow depth, total snowfall, and
    extreme maximum daily precipitation indicators.
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
- href: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-myanmar
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
  description: Daily Summaries of Precipitation Indicators for Myanmar (CSV)
  download_url: https://data.humdata.org/dataset/a17cad5b-e40b-491f-b215-3274e429eddf/resource/279d59b3-32a5-4ac2-aa25-cbcfbf967772/download/precipitation_mmr.csv
  format: null
  id: resource_279d59b3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: precipitation_mmr.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mmr_hdx_dailysummariesprecipitati_20151223
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-23'
temporal_resolution: null
title: Daily Summaries of Precipitation Indicators for Myanmar
version: null
vulnerability: null
---
