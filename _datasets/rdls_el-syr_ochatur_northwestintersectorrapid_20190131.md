---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Turkey
    url: https://data.humdata.org/dataset/north-west-syria-inter-sector-rapid-needs-assessment-flood-impact-january-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "OCHA T\xFCrkiye (inactive)"
  url: https://data.humdata.org/dataset/north-west-syria-inter-sector-rapid-needs-assessment-flood-impact-january-2019
creator:
  affiliation: null
  email: null
  name: "OCHA T\xFCrkiye (inactive)"
  url: https://data.humdata.org/dataset/north-west-syria-inter-sector-rapid-needs-assessment-flood-impact-january-2019
dataset_id: rdls_el-syr_ochatur_northwestintersectorrapid_20190131
description: 'On 26 December 2018, exceptionally heavy rainfall caused severe flash
  flooding in Idleb and Aleppo governorates in north-west Syria. This area has a high
  proportion of displaced people and concentration of camps and sites, making it a
  region with a notably large vulnerable population. Hundreds of tents were reportedly
  swept away and concrete houses in camps collapsed. As a result of the flooding,
  thousands of people have been impacted. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/north-west-syria-inter-sector-rapid-needs-assessment-flood-impact-january-2019]'
details: KEY FINDINGS The results of this assessment showed a critical need for repair
  and rehabilitation of infrastructure and social services impacted by the flood.
  74% of KIs reported partial damage to roads/streets as a result of the flood, and
  a majority of KIs (78%) reported a high priority need for repair/rehabilitation
  of roads/streets. The flooding impact has exacerbated pre-existing conditions and
  needs. Access to education for school-aged children among the population in assessed
  locations was found to be challenging. KIs in 34% of assessed IDP camps/sites and
  communities reported that less than 50% of school-aged children were attending school,
  with the top barrier to education reportedly being children working/children having
  to work. This assessment also showed a critical need for winterisation support.
  Winterisation kits were reported to be a priority by KIs (68%) when asked of top
  educational needs. Similarly, winter clothing kits were reported by KIs (97%) to
  be a top need when asked about shelter and NFI needs.
exposure:
- asset_type:
    description: Tent and concrete structures in camps and settlements affected by
      flooding
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
- asset_type:
    description: Displaced population and residents in camps and settlements in Idleb
      and Aleppo governorates
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Post-event rapid needs assessment conducted by OCHA following severe
    flash flooding on 26 December 2018 in north-west Syria. Data compiled from field
    assessments and reports documenting direct impacts on displaced populations, camps,
    and settlements in Idleb and Aleppo governorates, with focus on affected populations
    and damaged structures.
  sources:
  - id: source_1
    license: null
    name: OCHA Turkey
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/north-west-syria-inter-sector-rapid-needs-assessment-flood-impact-january-2019
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to tents and concrete structures in camps from flash
      flooding
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flash flooding in north-west Syria
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North-West Syria: Inter-Sector Rapid Needs Assessment - Flood Impact
    January 2019 (Excel)'
  download_url: https://data.humdata.org/dataset/ce0a540f-3f87-4fb7-9be3-2320f5ca00a1/resource/819fd2df-0525-44a2-afd3-07bb733599bc/download/nws_flood_rna_dataset_january2019_hdx.xlsx
  format: null
  id: resource_819fd2df
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NWS_Flood_RNA_Dataset_January2019_HDX.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North-West Syria: Inter-Sector Rapid Needs Assessment - Flood Impact
    January 2019 (PDF)'
  download_url: https://data.humdata.org/dataset/ce0a540f-3f87-4fb7-9be3-2320f5ca00a1/resource/1f68b7bb-91a4-4255-9755-c55b47f1d765/download/nws_flood_factsheet_rna_january2019_updated.pdf
  format: null
  id: resource_1f68b7bb
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NWS_Flood_Factsheet_RNA_January2019_updated.pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_ochatur_northwestintersectorrapid_20190131
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-01-31'
temporal_resolution: null
title: 'North-West Syria: Inter-Sector Rapid Needs Assessment - Flood Impact January
  2019'
version: null
vulnerability: null
---
