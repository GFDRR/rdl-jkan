---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Centers for Environmental Information (NCEI / NOAA)
    url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-iran--islamic-republic-of
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-iran--islamic-republic-of
creator:
  affiliation: null
  email: null
  name: National Centers for Environmental Information (NCEI / NOAA)
  url: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-iran--islamic-republic-of
dataset_id: rdls_hzd-irn_hdx_dailysummariesprecipitati_20151223
description: 'This dataset contains the daily summaries on base stations across Iran,
  Islamic Republic of . The four indicators included are: * TPCP : Total precipitation
  * MXSD : Maximum snow depth * TSNW : Total snow fall * EMXP : Extreme maximum daily
  precipitation Indicators are compiled by the National Centers for Environmental
  Information (NCEI), which is administrated by National Oceanic and Atmospheric Administration
  (NOAA) an organization part of the United States government. NOAA has access to
  data collected from thousands of base stations around the world, which collect data
  periodically on weather and climate conditions. This dataset contains the latest
  5 years of available data .. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-iran--islamic-republic-of]'
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
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Daily precipitation and snow observations were collected from meteorological
    base stations across Iran by NOAA's National Centers for Environmental Information.
    Stations were filtered to meet a minimum 30-year record requirement with at least
    182 complete days per year. Four indicators (total precipitation, maximum snow
    depth, total snowfall, extreme maximum daily precipitation) were extracted and
    compiled into daily summaries for drought and precipitation hazard characterization.
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
- href: https://data.humdata.org/dataset/daily-summaries-of-precipitation-indicators-for-iran--islamic-republic-of
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
  description: Daily Summaries of Precipitation Indicators for Iran, Islamic Republic
    of (CSV)
  download_url: https://data.humdata.org/dataset/d082061d-5340-4c7d-93f5-80daa900a061/resource/f769fab0-f0f8-4a2a-bfc7-5ba0a5de4f3a/download/precipitation_irn.csv
  format: null
  id: resource_f769fab0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: precipitation_irn.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-irn_hdx_dailysummariesprecipitati_20151223
spatial:
  bbox: null
  centroid: null
  countries:
  - IRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-23'
temporal_resolution: null
title: Daily Summaries of Precipitation Indicators for Iran, Islamic Republic of
version: null
vulnerability: null
---
