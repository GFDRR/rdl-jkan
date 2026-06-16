---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: World Health Organization
  url: https://data.humdata.org/dataset/climate-change-attributable-deaths
creator:
  affiliation: null
  email: null
  name: World Health Organization
  url: https://data.humdata.org/dataset/climate-change-attributable-deaths
dataset_id: rdls_lss-who_climatechangeattributable_2004
description: 'Climate Change Attributable Deaths. Climate Change Attributable Deaths
  Per Capita. Measuring the health effects from climate change can only be very approximate.
  Nevertheless, a assessment coordinated by WHO, taking into account only a subset
  of the possible health impacts, concluded that the modest climate change that has
  occurred since the 1970s was already causing over 140 000 excess deaths annually
  by the year 2004.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/climate-change-attributable-deaths]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: WHO coordinated a burden of disease assessment attributing excess mortality
    to climate change by integrating health impact data from multiple climate-related
    hazards. Deaths and DALYs were calculated as population health metrics reflecting
    premature mortality and disability from climate change exposure since the 1970s,
    with estimates of over 140,000 annual excess deaths by 2004.
  sources:
  - id: source_1
    license: null
    name: World Health Organization
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climate-change-attributable-deaths
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct mortality attributable to climate change and associated extreme
      temperature and weather events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Climate Change Attributable Deaths
  download_url: https://data.humdata.org/dataset/4b2ca75a-e24e-4f16-9098-77327bf9ecf2/resource/8502baa3-a6a5-4e4b-b834-ceacce1ff233/download/climate_change_attributable_deaths.csv
  format: null
  id: resource_8502baa3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Climate Change Attributable Deaths
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-who_climatechangeattributable_2004
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
  end: '2004-12-31'
  start: '2004-01-01'
temporal_resolution: null
title: Climate Change Attributable Deaths
version: null
vulnerability: null
---
