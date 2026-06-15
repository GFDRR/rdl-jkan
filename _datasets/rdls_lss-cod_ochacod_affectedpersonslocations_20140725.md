---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA et partenaires
    url: https://data.humdata.org/dataset/dr-congo-affected-persons-locations
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/dr-congo-affected-persons-locations
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/dr-congo-affected-persons-locations
dataset_id: rdls_lss-cod_ochacod_affectedpersonslocations_20140725
description: "Personnes d\xE9plac\xE9es internes, retour de population, refugi\xE9\
  s et rapatri\xE9s en RDC. Chiffres/ lieux de d\xE9placement des presonnes d\xE9\
  plac\xE9es internes, retourn\xE9s, r\xE9fugi\xE9s et rapatri\xE9s en RDC.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/dr-congo-affected-persons-locations]"
details: '**Languages:** FR'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Data compiled by OCHA and humanitarian partners from administrative
    records and field reports documenting internally displaced persons, returnees,
    refugees, and repatriated populations in DRC, with displacement locations and
    counts aggregated at settlement/administrative levels.
  sources:
  - id: source_1
    license: null
    name: OCHA et partenaires
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/dr-congo-affected-persons-locations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood and other hazards in DRC
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
    description: Returned population and refugees in DRC
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: DR Congo - Affected Persons Locations (Excel)
  download_url: https://data.humdata.org/dataset/fce36ec7-d010-4701-8f93-096b5a1e846e/resource/3d9118d1-a224-44f8-80b0-bc4252a6ca2f/download/rdc_synthese_idps25juin2015.xls
  format: null
  id: resource_3d9118d1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rdc_synthese_idps25juin2015.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DR Congo - Affected Persons Locations (ZIP archive)
  download_url: https://data.humdata.org/dataset/fce36ec7-d010-4701-8f93-096b5a1e846e/resource/76fb41e5-9ffb-41b7-9a0b-2ca43846cd5a/download/drc_factsheet_aout_2015_a3p.zip
  format: null
  id: resource_76fb41e5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: drc_factsheet_aout_2015_a3p.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DR Congo - Affected Persons Locations (ZIP archive)
  download_url: https://data.humdata.org/dataset/fce36ec7-d010-4701-8f93-096b5a1e846e/resource/8f3327e7-44ff-496d-923a-6db4600b1e4b/download/refugee_factsheet_31_08_2015.zip
  format: null
  id: resource_8f3327e7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: refugee_factsheet_31_08_2015.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DR Congo - Affected Persons Locations (ZIP archive)
  download_url: https://data.humdata.org/dataset/fce36ec7-d010-4701-8f93-096b5a1e846e/resource/3bc5ceb4-e166-4de2-b434-83c84bf8fcbd/download/repatriation_factsheet_31_08_2015.zip
  format: null
  id: resource_3bc5ceb4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: repatriation_factsheet_31_08_2015.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_affectedpersonslocations_20140725
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-07-25'
temporal_resolution: null
title: DR Congo - Affected Persons Locations
version: null
vulnerability: null
---
