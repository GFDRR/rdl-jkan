---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/ZENODO.8269680
creator:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/ZENODO.8269680
dataset_id: rdls_hzd-crstac_myriadhazardeventssetsmyriadhes_multihazardeventssets
description: 'A global multi-hazard event set database, spanning from 2004 to 2017,
  which includes eleven hazards (coldwaves, heatwaves, droughts, earthquakes, extreme
  wind events, floods, landslides, tropical cyclones, tsunamis, volcanic eruptions,
  and wildfires) [Source: This metadata record was automatically extracted from the
  STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: A global multi-hazard event set database, spanning from 2004 to 2017,
    which includes eleven hazards (coldwaves, heatwaves, droughts, earthquakes, extreme
    wind events, floods, landslides, tropical cyclones, tsunamis, volcanic eruptions,
    and wildfires).
  sources:
  - id: source_underlying_1
    license: null
    name: variety of datasets
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_underlying_2
    license: null
    name: partially included in this catalog as well
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://doi.org/10.5281/zenodo.8272754
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/ZENODO.8269680
purpose: Calculated with the MYRIAD - Hazard Event Sets Algorithm (MYRIAD-HESA); also
  includes non-climatic hazards (i.e. earthquakes, volcanic eruptions)
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41598-023-40400-5
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41598-023-40400-5
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/multi-hazard/myriad-hazard-events-sets-myriad-hes/multi-hazard-events-sets/multi-hazard-events-sets.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: event level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: MYRIAD Hazard Events Sets (MYRIAD-HES) - Multi-hazard events
    sets'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: MYRIAD Hazard Events Sets (MYRIAD-HES) - Multi-hazard events sets -
    data file
  download_url: https://zenodo.org/records/8269680/files/MYRIAD-HES.zip?download=1
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: event level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYRIAD Hazard Events Sets (MYRIAD-HES) - Multi-hazard events sets - data
    file
- access_url: https://doi.org/10.1038/s41598-023-40400-5
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: MYRIAD Hazard Events Sets (MYRIAD-HES) - Multi-hazard events sets (Web
    reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: event level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
- access_url: https://doi.org/10.5281/zenodo.8272754
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: MYRIAD Hazard Events Sets (MYRIAD-HES) - Multi-hazard events sets (Code
    link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: event level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_myriadhazardeventssetsmyriadhes_multihazardeventssets
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017'
  start: '2004'
temporal_resolution: null
title: MYRIAD Hazard Events Sets (MYRIAD-HES) - Multi-hazard events sets
version: null
vulnerability: null
---
