---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Global Climate Forum
  url: https://globalclimateforum.org/
creator:
  affiliation: null
  email: null
  name: Global Climate Forum
  url: https://globalclimateforum.org/
dataset_id: rdls_vln-coclico_cbahr
description: 'We determine efficient coastal adaptation pathways for each coastal
  floodplain management unit at the European coastline based on a dynamic (inter-temporal)
  cost-benefit analysis. Protection, retreat and accommodation are considered as potential
  adaptation options; the height of a protection measure and the retreat height under
  which all people and assets retreat are determined by the optimisation. Accommodation
  is binary; buildings can be flood-proofed by up to an extreme event of one meter.
  The output of this cost-benefit analysis are the most cost-efficient adaptation
  trajectories, including adaptation options and their height per time step for each
  floodplain. We further provide the expected residual flood damages and adaptation
  costs in US$2024. This could be useful to coastal decision-makers to initiate coastal
  adaptation processes and for global institutions to estimate costs on coastal adaptation
  on global scale. It is used for a publication that will be send to Nature Climate
  Change. The files ''GCF.open.CBA_country.SSP245'' included aggregated information
  based on the detailed trajectories on country level. The ending ''SSP126'' defines
  the shared socioeconomic pathway that was used. The variables are the following:
  country (country name), nuts (EU NUTS two letter code), coast_length (coast length
  of that country in our model in km), protection_2050 (proportion of the entire coastline
  of that country where protection is efficient in the year 2050), retreat_2050 (proportion
  of the entire coastline of that country where retreat is efficient in the year 2050),
  acc_2050 (proportion of the entire coastline of that country where accommodation
  is efficient in the year 2050), protection_retreat_2050 (proportion of the entire
  coastline of that country where protection&retreat simultaneously is efficient in
  the year 2050), no_adaptation_2050 (proportion of the entire coastline of that country
  where no adaptation is efficient in the year 2050), costs_adaptation (the costs
  for implementing and maintaining adaptation options over the entire time horizon
  from 2020-2150), costs_damage (the costs for (residual) flood damage over the entire
  time horizon from 2020-2150), costs= costs_adaptation + costs_damage The files ''GCF.open.CBA.SSP126''
  contain the detailed adaptation trajectories for each floodplain and all time steps.
  The ending SSP126 defines the shared socioeconomic pathway that was used. The variables
  are the following: fpid (ID of each floodplain), year (year), protection_height
  (efficient protection height for specific floodplain and year), protection_level
  (return period of this protection height), retreat_height (efficient retreat height
  for specific floodplain and year), accommodation (efficient binary indicator for
  accommodation for specific floodplain and year), total_costs (= total_adaptation_costs
  + total_flood_damages), total_adaptation_costs (adaptation costs, including maintenance,
  for this floodplain under the efficient adaptation trajectory for year x until 2150),
  total_flood_damages (flood damages for this floodplain under the efficient adaptation
  trajectory for year x until 2150), current_adaptation_cost (adaptation costs for
  this floodplain under the efficient adaptation trajectory at specific year x), annual_flood_damage
  (flood damage for this floodplain under the efficient adaptation trajectory at specific
  year x). Variants in the source dataset - adaptation strategy: SSP126, SSP245, SSP585.
  [Source: This metadata record was automatically extracted from the STAC catalog
  coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: 'We determine efficient coastal adaptation pathways for each coastal
    floodplain management unit at the European coastline based on a dynamic (inter-temporal)
    cost-benefit analysis. Protection, retreat and accommodation are considered as
    potential adaptation options; the height of a protection measure and the retreat
    height under which all people and assets retreat are determined by the optimisation.
    Accommodation is binary; buildings can be flood-proofed by up to an extreme event
    of one meter. The output of this cost-benefit analysis are the most cost-efficient
    adaptation trajectories, including adaptation options and their height per time
    step for each floodplain. We further provide the expected residual flood damages
    and adaptation costs in US$2024. This could be useful to coastal decision-makers
    to initiate coastal adaptation processes and for global institutions to estimate
    costs on coastal adaptation on global scale. It is used for a publication that
    will be send to Nature Climate Change. The files ''GCF.open.CBA_country.SSP245''
    included aggregated information based on the detailed trajectories on country
    level. The ending ''SSP126'' defines the shared socioeconomic pathway that was
    used. The variables are the following: country (country name), nuts (EU NUTS two
    letter code), coast_length (coast length of that country in our model in km),
    protection_2050 (proportion of the entire coastline of that country where protection
    is efficient in the year 2050), retreat_2050 (proportion of the entire coastline
    of that country where retreat is efficient in the year 2050), acc_2050 (proportion
    of the entire coastline of that country where accommodation is efficient in the
    year 2050), protection_retreat_2050 (proportion of the entire coastline of that
    country where protection&retreat simultaneously is efficient in the year 2050),
    no_adaptation_2050 (proportion of the entire coastline of that country where no
    adaptation is efficient in the year 2050), costs_adaptation (the costs for implementing
    and maintaining adaptation options over the entire time horizon from 2020-2150),
    costs_damage (the costs for (residual) flood damage over the entire time horizon
    from 2020-2150), costs= costs_adaptation + costs_damage The files ''GCF.open.CBA.SSP126''
    contain the detailed adaptation trajectories for each floodplain and all time
    steps. The ending SSP126 defines the shared socioeconomic pathway that was used.
    The variables are the following: fpid (ID of each floodplain), year (year), protection_height
    (efficient protection height for specific floodplain and year), protection_level
    (return period of this protection height), retreat_height (efficient retreat height
    for specific floodplain and year), accommodation (efficient binary indicator for
    accommodation for specific floodplain and year), total_costs (= total_adaptation_costs
    + total_flood_damages), total_adaptation_costs (adaptation costs, including maintenance,
    for this floodplain under the efficient adaptation trajectory for year x until
    2150), total_flood_damages (flood damages for this floodplain under the efficient
    adaptation trajectory for year x until 2150), current_adaptation_cost (adaptation
    costs for this floodplain under the efficient adaptation trajectory at specific
    year x), annual_flood_damage (flood damage for this floodplain under the efficient
    adaptation trajectory at specific year x)'
  sources:
  - id: source_1
    license: null
    name: Global Climate Forum
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://globalclimateforum.org/
    used_in: vulnerability
  - id: source_2
    license: null
    name: Deltares
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://deltares.nl
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Global Climate Forum
  url: https://globalclimateforum.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: "V\xC3\xB6lz, V., Lincke, D., Hinkel, J., Honsel, L. (2024). Efficient adaptation\
    \ pathways for European floodplains. tbd"
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cba_hr/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cba_hr/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Cost-benefit analysis of coastal adaptation per
    floodplain [cba_hr]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fcba_hr.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Cost-benefit analysis of coastal adaptation per floodplain
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Cost-benefit analysis of coastal adaptation per floodplain
    (Snapshot of the collection's STAC items exported to GeoParquet format.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/GCF.open.CBA.SSP126.floodplain.parquet
  format: null
  id: resource_geoparquetstacitems
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoParquet STAC items
risk_data_type:
- vulnerability
schema: rdls-10
slug: rdls_vln-coclico_cbahr
spatial:
  bbox:
  - -31.149830017979554
  - 27.735655444173794
  - 34.55397102401321
  - 71.1079899560078
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020'
  start: '2020'
temporal_resolution: null
title: CoCliCo - Cost-benefit analysis of coastal adaptation per floodplain
version: null
vulnerability: null
---
