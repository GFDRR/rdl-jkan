---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/preliminary-internal-displacement-updates
creator:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/preliminary-internal-displacement-updates
dataset_id: rdls_lss-idmc_preliminaryupdatesapi
description: 'The IDMC''s Internal Displacement Updates (IDU) are preliminary estimates
  of new displacements reported in the last 180 days. The IDU API presents provisional
  data that is updated on daily basis, according to the availability of data. Curated
  and validated estimates are published in the Global Internal Displacement Database
  (GIDD) -See https://www.internaldisplacement.org/database/displacement-data. For
  a detailed description of methodology please refer to the IDMC GRID methodological
  annex (https://www.internal-displacement.org/global-report/grid2020/downloads/2020-IDMC-GRID-methodology.pdf)
  and IDMC''s monitoring guidelines (https://monitoringguidance.wixsite.com/idmc).
  The IDU dataset contains preliminary estimates of aggregated from diverse publishers
  or sources. New displacement estimates are provided for three different causes of
  internal displacement: disasters, conflict and violence, and development projects.
  The documentation of the API is available at bit.ly/IDU_API_DOC.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-internal-displacement-updates]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IDMC collects and validates reports of new internal displacements from
    multiple hazard types over rolling 180-day windows. Preliminary estimates are
    aggregated by event, location, and hazard type, then published via API with daily
    updates. Data undergoes quality assurance before inclusion in the authoritative
    Global Internal Displacement Database.
  sources:
  - id: source_1
    license: null
    name: Internal Displacement Monitoring Centre (IDMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-internal-displacement-updates
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internal displacement counts from flood events reported in the last
      180 days
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internal displacement counts from earthquake events reported in the
      last 180 days
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internal displacement counts from strong wind/cyclone events reported
      in the last 180 days
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internal displacement counts from wildfire events reported in the
      last 180 days
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internal displacement counts from drought events reported in the
      last 180 days
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.internal-displacement.org/database/methodology
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary Internal Displacement Updates API (CSV)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vSjAww1Xd-kHg5NKVZknWXJElWIrOSHnWitOaryYgaAjTGCrCr2Ev8ygl2Z4ROlKz8zMR_DsllDzyD0/pub?gid=0&single=true&output=csv
  format: null
  id: resource_1ace9c2a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idus_view_flat.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary Internal Displacement Updates API (JSON)
  download_url: https://backend.idmcdb.org/data/idus_view_flat
  format: null
  id: resource_f5fd5b73
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idus_view_flat.json
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary Internal Displacement Updates API (GeoJSON)
  download_url: https://backend.idmcdb.org/api/idus-view-flat-geojson
  format: null
  id: resource_2338437e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idus-view-flat-geojson.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary Internal Displacement Updates API (PDF)
  download_url: https://www.internal-displacement.org/sites/default/files/IDMC_IDU_API_Codebook_14102020.pdf
  format: null
  id: resource_a93bccf7
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HDX_IDU_Codebook_19052020_V1.pdf
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idmc_preliminaryupdatesapi
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Preliminary Internal Displacement Updates API
version: null
vulnerability: null
---
