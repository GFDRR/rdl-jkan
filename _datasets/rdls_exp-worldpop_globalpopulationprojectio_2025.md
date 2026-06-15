---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Global2 R2025A
    url: https://data.humdata.org/dataset/futurepop_1km_grid_population_2025-2100_ssp_v0_2
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Shared Socioeconomic Pathways (SSP) 3.2
    url: https://data.humdata.org/dataset/futurepop_1km_grid_population_2025-2100_ssp_v0_2
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/futurepop_1km_grid_population_2025-2100_ssp_v0_2
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/futurepop_1km_grid_population_2025-2100_ssp_v0_2
dataset_id: rdls_exp-worldpop_globalpopulationprojectio_2025
description: 'This data release provides gridded population distributions (spatial
  resolution of 30 arc-seconds, approximately 1km grid cells) globally for 2025-2100,
  quantitatively consistent with the Shared Socioeconomic Pathways (SSP) 3.2 national
  population scenarios. National population totals at 5-year intervals for 2025-2100
  were provided for each SSP scenario. Using WorldPop Global2 R2025A data , subnational
  population proportions were calculated and summarised at administrative unit level
  2, i.e. the percentage of the national population within each administrative unit.
  Global2 historical settlement data was used to determine the percentage of grid
  cells that became built settlement per administrative unit in 5-year intervals for
  2015-2025 and the number of people per new settlement grid cell. This rate of settlement
  change was extrapolated into future 5-year intervals (2030-2100) and cross-referenced
  against a probability of becoming built settlement layer, where the transition probability
  of non-built-settlement to built-settlement was created following the methodology
  outlined in Nieves, J. J., etc . The grid cells with the highest probability of
  becoming built settlement were selected until the required percentage of grid cells
  was reached. The WorldPop Global2 R2025A population data were populated with new
  settlement grid cells and normalised so that the national population count was consistent
  with the SSP totals. Concurrently, the subnational population proportions calculated
  at administrative unit level 2 were retained during normalisation. These steps were
  implemented to create the global gridded population distributions for 2015-2100
  for each SSP scenario. These data were produced by the WorldPop Research Group at
  the University of Southampton in collaboration with researchers at the University
  of Bristol. This work was part of the FuturePop: Constructing high spatial resolution
  population projections and supporting the provision, access and updates of WorldPop
  spatial demographic datasets project, funded by the Wellcome Trust (grant 308679/Z/23/Z).
  For more details about the datasets, please refer to the release statement here.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/futurepop_1km_grid_population_2025-2100_ssp_v0_2]'
details: '###Recommended citation Bondarenko M., Tejedor-Garavito N., Priyatikanto
  R., Zhang W., Fang W., Nosatiuk B., Gaskell J., McKeen T., Noi E., Hilton J., Butterick
  J., Hawker L., Tatem A. J.. ''Global 1km-grid population projections for 2025-2100
  consistent with the Shared Socioeconomic Pathways 3.2 national population projections,
  version 0.2'' 2025 doi:10.5258/SOTON/WP00849'
exposure:
- asset_type:
    description: Gridded population projections at 1 km resolution for 2025-2100 under
      five Shared Socioeconomic Pathways scenarios
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: National population totals from SSP scenarios (2025-2100, 5-year intervals)
    were spatially disaggregated using subnational population proportions derived
    from WorldPop Global2 R2025A baseline data at administrative unit level 2, with
    settlement grid cells updated and normalized to ensure consistency with SSP national
    totals at 1 km resolution.
  sources:
  - id: source_1
    license: null
    name: WorldPop Global2 R2025A
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Shared Socioeconomic Pathways (SSP) 3.2
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/futurepop_1km_grid_population_2025-2100_ssp_v0_2
  rel: source
loss:
  losses: []
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
  url: https://data.worldpop.org/repo/prj/FuturePop/SSPs_1km_v0_2/Release_Statement_FP_SSPs_1km_v0_2.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 16 geotiff rasters at a spatial resolution of
    30 arc-seconds (approximately 1km). Each raster provides gridded population for
    2025-2100 consistent with the SSP1.
  download_url: https://data.worldpop.org/repo/prj/FuturePop/SSPs_1km_v0_2/FuturePop_SSP1_1km_v0_2.zip
  format: null
  id: resource_4b2530b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FuturePop_SSP1_1km_v0_2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 16 geotiff rasters at a spatial resolution of
    30 arc-seconds (approximately 1km). Each raster provides gridded population for
    2025-2100 consistent with the SSP2.
  download_url: https://data.worldpop.org/repo/prj/FuturePop/SSPs_1km_v0_2/FuturePop_SSP2_1km_v0_2.zip
  format: null
  id: resource_1ff06b4a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FuturePop_SSP2_1km_v0_2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 16 geotiff rasters at a spatial resolution of
    30 arc-seconds (approximately 1km). Each raster provides gridded population for
    2025-2100 consistent with the SSP3.
  download_url: https://data.worldpop.org/repo/prj/FuturePop/SSPs_1km_v0_2/FuturePop_SSP3_1km_v0_2.zip
  format: null
  id: resource_f8e3a57b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FuturePop_SSP3_1km_v0_2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 16 geotiff rasters at a spatial resolution of
    30 arc-seconds (approximately 1km). Each raster provides gridded population for
    2025-2100 consistent with the SSP4.
  download_url: https://data.worldpop.org/repo/prj/FuturePop/SSPs_1km_v0_2/FuturePop_SSP4_1km_v0_2.zip
  format: null
  id: resource_d80f5d88
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FuturePop_SSP4_1km_v0_2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 16 geotiff rasters at a spatial resolution of
    30 arc-seconds (approximately 1km). Each raster provides gridded population for
    2025-2100 consistent with the SSP5.
  download_url: https://data.worldpop.org/repo/prj/FuturePop/SSPs_1km_v0_2/FuturePop_SSP5_1km_v0_2.zip
  format: null
  id: resource_a031a526
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FuturePop_SSP5_1km_v0_2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Population Projections (1 km Grid) (For more details about the
    datasets, please refer to the release statement.)
  download_url: https://data.worldpop.org/repo/prj/FuturePop/SSPs_1km_v0_2/Release_Statement_FP_SSPs_1km_v0_2.pdf
  format: null
  id: resource_4611e353
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Release_Statement_FP_SSPs_1km_v0_2.pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-worldpop_globalpopulationprojectio_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2100-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: Global Population Projections (1 km Grid)
version: null
vulnerability: null
---
