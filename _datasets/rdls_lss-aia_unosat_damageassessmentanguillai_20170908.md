---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-anguilla-island-as-of-8-september-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-anguilla-island-as-of-8-september-2017
dataset_id: rdls_lss-aia_unosat_damageassessmentanguillai_20170908
description: 'This dataset illustrates satellite-detected potential damaged buildings
  in Anguilla Island, following the landfall of Tropical Cyclone IRMA-17 on September
  6, 2017. The UNITAR-UNOSAT analysis used a Kompsat-3 satellite image acquired on
  9 February 2017 and WorldView-2 image acquired on 5 July 2017 as pre-imagery and
  Pleiades satellite imagery acquired on the 7 & 8 September 2017 as a post-imagery.
  The UNITAR-UNOSAT analysis identified 2,147 potentially damaged structures within
  the analyzed area that was not covered by clouds. According to the pre-building
  footprints, inside the area free of clouds, provided by Humanitarian Open Street
  Map, this represents 42% of potentially affected structures in Anguilla.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-anguilla-island-as-of-8-september-2017]'
details: This is a preliminary analysis and has not yet been validated in the field.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT conducted post-event satellite image analysis comparing pre-event
    imagery (Kompsat-3 from February 2017, WorldView-2 from July 2017) with post-event
    Pleiades imagery (7-8 September 2017) to detect and classify building damage following
    Tropical Cyclone IRMA-17 landfall on 6 September 2017. Damaged structures were
    identified through visual interpretation and confidence-rated classification within
    cloud-free areas.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-anguilla-island-as-of-8-september-2017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone IRMA-17 detected via
      satellite imagery
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
        metric: loss
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Anguilla Island as of 8 September 2017 (Shapefile)
  download_url: https://data.humdata.org/dataset/4b52d9d9-3c03-4ba6-a2cc-54b0896d1c6d/resource/534e489c-f7ee-4573-b7f1-a076a254831b/download/anguila_building_damage_assessment_8sept.zip
  format: null
  id: resource_534e489c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Anguila_building_damage_assessment_8sept.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-aia_unosat_damageassessmentanguillai_20170908
spatial:
  bbox: null
  centroid: null
  countries:
  - AIA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-08'
temporal_resolution: null
title: Damage Assessment in Anguilla Island as of 8 September 2017
version: null
vulnerability: null
---
