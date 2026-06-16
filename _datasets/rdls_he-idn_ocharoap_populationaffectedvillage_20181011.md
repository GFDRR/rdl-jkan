---
attributions:
- entity:
    affiliation: null
    email: null
    name: BPS (Badan Pusat Statistik - Statistics Indonesia)
    url: https://data.humdata.org/dataset/central-sulawesi-population-2017
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Shakemap (USGS/Indonesian Geological Agency)
    url: https://data.humdata.org/dataset/central-sulawesi-population-2017
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/central-sulawesi-population-2017
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/central-sulawesi-population-2017
dataset_id: rdls_he-idn_ocharoap_populationaffectedvillage_20181011
description: 'The spreadsheet have 2 worksheet (Pop and Geoimpact). Geoimpact is the
  result of overlaying the shakemap with admin4 (village) boundaries from BPS. This
  processing and analysis was done by the World Food Programme (WFP).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/central-sulawesi-population-2017]'
details: The datasets only contain areas experience mmi 5 above.
exposure:
- asset_type:
    description: "Population of villages exposed to earthquake ground motion (MMI\
      \ \xE2\u2030\xA55)"
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
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Observed shakemap from the 2017 Central Sulawesi earthquake was spatially
    overlaid with village-level administrative boundaries and census population data
    from BPS by WFP to identify populations exposed to ground motion intensities of
    MMI 5 and above.
  sources:
  - id: source_1
    license: null
    name: BPS (Badan Pusat Statistik - Statistics Indonesia)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Shakemap (USGS/Indonesian Geological Agency)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-sulawesi-population-2017
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This data is extracted from the SIAK database (Population Information
    Administration System - https://id.wikipedia.org/wiki/Sistem_informasi_administrasi_kependudukan)
    of the Ministry of Home Affairs - MoHA. The data is served as GIS REST Services
    and is available publicly.
  download_url: https://data.humdata.org/dataset/8622492e-0108-4569-8aae-3a4316871dcf/resource/f826ca43-91a9-45d4-b9c5-52dbab7446aa/download/palu_eq_pop_adm4_mmi5above_kemendagri_2017.xlsx
  format: null
  id: resource_f826ca43
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palu_eq_pop_adm4_mmi5above_kemendagri_2017.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_ocharoap_populationaffectedvillage_20181011
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-10-11'
temporal_resolution: null
title: Indonesia - Population of Affected Villages of Central Sulawesi EQ
version: null
vulnerability: null
---
