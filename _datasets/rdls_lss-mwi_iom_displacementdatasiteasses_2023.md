---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-cyclone-freddy-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-cyclone-freddy-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-cyclone-freddy-iom-dtm
dataset_id: rdls_lss-mwi_iom_displacementdatasiteasses_2023
description: 'A site assessment is a sub-component of mobility tracking. It aims to
  collect data on population presence, living conditions and needs in a particular
  displacement site or community.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-cyclone-freddy-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted site assessments in displacement locations affected
    by Cyclone Freddy using standardized DTM methodology to enumerate displaced populations
    and document living conditions and needs in affected sites.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-cyclone-freddy-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population from Cyclone Freddy recorded in site assessments
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  url: https://displacement.iom.int/sites/default/files/public/Methodological%20Framework%20used%20in%20DTM%20Operations%20for%20Quantifying%20Displacement%20and%20Mobility.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The assessments were carried out following Tropical Cyclone Freddy,
    which hit the Southern region of Malawi on 12 March 2023 affecting at least 14
    districts. The most affected districts are Blantyre, Chikwawa, Nsanje, Mulanje,
    Phalombe Zomba and Mangochi. Over 426,04 families had their shelters completely/partially
    destroyed as a result of flash floods and Landslide caused by TC Freddy, displacing
    over 500,000 individuals to at least 500 camp/collective sites.
  download_url: https://data.humdata.org/dataset/da07a1be-f5e2-43c0-9956-53fcd50e3d53/resource/6332355d-ec41-4136-bb12-42bbb8bc0c28/download/dtm_malawi_msla_cyclone_freddy_round_1_20240425_public_all-new-hdx.xlsx
  format: null
  id: resource_6332355d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Malawi Site Assessment - Cyclone Freddy - Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mwi_iom_displacementdatasiteasses_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-04-27'
  start: '2023-03-31'
temporal_resolution: null
title: Malawi Displacement Data - Site Assessment - Cyclone Freddy - [IOM DTM]
version: null
vulnerability: null
---
