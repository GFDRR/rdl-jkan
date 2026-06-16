---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/evaluation-des-degats-a-taroudant-region-de-taroudant-province-de-souss-massa-maroc-au-10-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evaluation-des-degats-a-taroudant-region-de-taroudant-province-de-souss-massa-maroc-au-10-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evaluation-des-degats-a-taroudant-region-de-taroudant-province-de-souss-massa-maroc-au-10-
dataset_id: rdls_lss-mar_unosat_evaluationdesdegatstaroud_20230911
description: "UNOSAT code EQ20230909MAR, GDACS Id: 1390643 Cette carte illustre les\
  \ structures/b\xE2timents potentiellement endommag\xE9s par le s\xE9isme du 8 Septembre\
  \ 2023 \xE0 Taroudant (\xE0 155 km au SO de Marrakech) tel qu'observ\xE9 \xE0 partir\
  \ de l'analyse d'une image satellite Pl\xE9iades acquise le 10 Septembre 2023. Dans\
  \ ce secteur d'analyse, UNOSAT a identifi\xE9 205 b\xE2timents endommag\xE9s et/ou\
  \ potentiellement endommag\xE9s. L'observation d'un regroupement de tentes au NE\
  \ de la ville indiquerait une zone de rassemblement temporaire de sinistr\xE9s.\
  \ Ceci est une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur\
  \ le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires au Centre Satellitaire\
  \ des Nations Unies (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/evaluation-des-degats-a-taroudant-region-de-taroudant-province-de-souss-massa-maroc-au-10-]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared Pl\xE9iades satellite imagery acquired on\
    \ 10 September 2023 with pre-event imagery to identify structural damage from\
    \ the 8 September 2023 earthquake. Visual change detection methods identified\
    \ 205 damaged/potentially damaged buildings in the Taroudant study area, with\
    \ supplementary observations of temporary displacement camps indicating affected\
    \ population concentration."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/evaluation-des-degats-a-taroudant-region-de-taroudant-province-de-souss-massa-maroc-au-10-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 8 September 2023 earthquake
      in Taroudant, identified through satellite imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Morocco - \xC9valuation des d\xE9gats \xE0 Taroudant, r\xE9gion de\
    \ Taroudant, province de Souss Massa, Maroc, au 10 Septembre 2023 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3667/EQ20230909MAR_gdb.zip
  format: Geodatabase
  id: resource_0c516e68
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Morocco - \xC9valuation des d\xE9gats \xE0 Taroudant, r\xE9gion de\
    \ Taroudant, province de Souss Massa, Maroc, au 10 Septembre 2023 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3667/EQ20230909MAR_SHP.zip
  format: null
  id: resource_5cc3f908
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mar_unosat_evaluationdesdegatstaroud_20230911
spatial:
  bbox: null
  centroid: null
  countries:
  - MAR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-11'
temporal_resolution: null
title: "Morocco - \xC9valuation des d\xE9gats \xE0 Taroudant, r\xE9gion de Taroudant,\
  \ province de Souss Massa, Maroc, au 10 Septembre 2023"
version: null
vulnerability: null
---
