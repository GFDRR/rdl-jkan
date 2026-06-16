---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNISDR
    url: https://data.humdata.org/dataset/tsunami-hazard-run-up-rp-500-years
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/tsunami-hazard-run-up-rp-500-years
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/tsunami-hazard-run-up-rp-500-years
dataset_id: rdls_hzd-undrr_globalmodeltsunamihazardr_20150101
description: 'Global model of tsunami hazard (run up) return period of 500 years..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tsunami-hazard-run-up-rp-500-years]'
details: This dataset was generated using other global datasets; it should not be
  used for local applications (such as land use planning). The main purpose of GAR
  2015 datasets is to broadly identify high risk areas at global level and for identification
  of areas where more detailed data should be collected. Some areas may be underestimated
  or overestimated. Given this analysis was conducted using global datasets, the resolution
  of which is not sufficient for in-situ planning, it should not be used for critical
  (like life saving) decisions. UNISDR and collaborators should in no case be liable
  for misuse or misinterpretation of the presented results. The designations employed
  and the presentation of material on the maps do not imply the expression of any
  opinion whatsoever on the part of UNISDR or the Secretariat of the United Nations
  concerning the legal status of any country, territory, city or area or of its authorities,
  or concerning the delimitation of its frontiers or boundaries. The designations
  employed and the presentation of material on the maps do not imply the expression
  of any opinion whatsoever on the part of UNISDR or the Secretariat of the United
  Nations concerning the legal status of any country, territory, city or area or of
  its authorities, or concerning the delimitation of its frontiers or boundaries.
  This analysis was conducted using global datasets, the resolution of which is not
  relevant for in-situ planning and should not be used for life and death decisions.
  UNISDR and collaborators should in no case be liable for misuse of the presented
  results.
exposure: []
hazard:
  event_sets_by_hazard_type:
    tsunami:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: Probabilistic tsunami hazard model with run-up heights at 500-year
          return period
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_tsunami
          intensity_measure: wd:m
          process: tsunami
          trigger: null
          type: tsunami
        id: event_500yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.002
            probability: null
            return_period: 500
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: tsunami
        trigger: null
        type: tsunami
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Global tsunami hazard model generated using UNISDR's integrated global
    datasets and modeling methodology to produce probabilistic run-up heights at 500-year
    return period, representing inundation depth hazard across coastal zones worldwide.
  sources:
  - id: source_1
    license: null
    name: UNISDR
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tsunami-hazard-run-up-rp-500-years
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
  description: Global model of tsunami hazard (run up) return period of 500 years
    (Zipped file of tsunami run up (39,557 kb).)
  download_url: https://data.humdata.org/dataset/0ab99df0-17d4-4582-9e16-790308905993/resource/fa1cd272-e6ea-4160-abfd-10fcbb43a398/download/tsunami-runup-rp500.zip
  format: null
  id: resource_fa1cd272
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tsunami_RunUp_RP500.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-undrr_globalmodeltsunamihazardr_20150101
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
  end: null
  start: '2015-01-01'
temporal_resolution: null
title: Global model of tsunami hazard (run up) return period of 500 years
version: null
vulnerability: null
---
