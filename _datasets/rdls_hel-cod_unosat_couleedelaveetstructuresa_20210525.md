---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc
dataset_id: rdls_hel-cod_unosat_couleedelaveetstructuresa_20210525
description: "UNOSAT code: VO20210523COD Cette carte illustre les structures et b\xE2\
  timents potentiellement impact\xE9es par la coul\xE9e de lave dans le district de\
  \ Nyiragongo, province du Nord-Kivu en R\xE9publique D\xE9mocratique du Congo suite\
  \ \xE0 l'\xE9ruption du volcan Nyiragongo du 22 mai 2021. A partir de l'analyse\
  \ d'une image radar TerraSAR-X acquise le 24 mai 2021 \xE0 16:13 UTC, UNITAR-UNOSAT\
  \ a observ\xE9 une coul\xE9e de lave qui s'est arr\xEAt\xE9e \xE0 700m des installations\
  \ a\xE9roportuaires. Sur l'\xE9tendue de l'analyse, environ 1,600 structures sont\
  \ potentiellement impact\xE9es par la coul\xE9e de lave \xE0 la date d'acquisition\
  \ de l'image radar. Ceci est une analyse pr\xE9liminaire et n'a pas encore \xE9\
  t\xE9 valid\xE9e sur le terrain. Veuillez d'envoyer vos commentaires \xE0 UNITAR-UNOSAT.\
  \ Note: L'analyse de coul\xE9e de lave \xE0 partir d'une image radar peut surestimer\
  \ la trace de la coul\xE9e de lave \xE0 cause du coefficient de r\xE9trodiffusion\
  \ du signal radar.. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building structures in Nyiragongo district potentially impacted by
      lava flow
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
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
      intensity_measure: h_vaf:mm
      process: lava
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed TerraSAR-X radar imagery from 24 May 2021
    to delineate the lava flow extent from the Nyiragongo eruption and overlay building
    footprints to identify structures within the hazard zone. The analysis identified
    approximately 1,600 buildings potentially impacted by the lava flow that had advanced
    to within 700 m of airport installations.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from lava flow inundation, approximately 1,600
      structures affected
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: "Coul\xE9e de lave et structures affect\xE9es suite \xE0 l'\xE9ruption\
    \ volcanique du Nyiragongo, Province du Nord-Kivu, RD Congo (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/CD/VO20210523COD/VO20210523COD_gdb.zip
  format: Geodatabase
  id: resource_fbd5b88b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20210523COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Coul\xE9e de lave et structures affect\xE9es suite \xE0 l'\xE9ruption\
    \ volcanique du Nyiragongo, Province du Nord-Kivu, RD Congo (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/CD/VO20210523COD/VO20210523COD_SHP.zip
  format: null
  id: resource_b386fcc9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20210523COD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cod_unosat_couleedelaveetstructuresa_20210525
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
  start: '2021-05-25'
temporal_resolution: null
title: "Coul\xE9e de lave et structures affect\xE9es suite \xE0 l'\xE9ruption volcanique\
  \ du Nyiragongo, Province du Nord-Kivu, RD Congo"
version: null
vulnerability: null
---
