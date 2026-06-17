---
attributions:
- entity:
    affiliation: null
    email: info@globalquakemodel.org
    name: GEM Foundation
    url: https://www.globalquakemodel.org/
  id: attribution_creator_gem
  role: creator
- entity:
    affiliation: null
    email: msuwa@worldbank.org
    name: Makoto Suwa
    url: https://www.worldbank.org
  id: attribution_ttl1
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: csoto@worldbank.org
    name: Claudia Soto
    url: https://www.worldbank.org
  id: attribution_ttl2
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: rreid1@worldbank.org
    name: Robert Reid
    url: https://www.worldbank.org
  id: attribution_ttl3
  role: world_bank_team_lead
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: pchrzanowski@worldbank.org
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  affiliation: null
  email: James.Allard@jbarisk.com
  name: JBA Risk Management Limited
  url: https://www.jbarisk.com/
dataset_id: rdls_hel-sle_freetownfloodrisk
description: Complete probabilistic flood risk assessment for Freetown including high-resolution
  hazard maps (1m river and surface water flooding), building exposure data (153,436
  buildings from GEM Foundation GED4ALL), and comprehensive loss metrics (AAL, OEP,
  AEP, ELT, PLT). Commissioned by World Bank to support climate and disaster risk
  management in Sierra Leone.
details: 'This comprehensive flood risk assessment combines: (1) JBA''s high-resolution
  (1m) probabilistic flood hazard maps for both river and surface water flooding across
  6 return periods (RP20-RP1500); (2) GEM Foundation''s building exposure database
  (GED4ALL taxonomy) with 153,436 georeferenced buildings valued at USD $8.08 billion;
  and (3) complete catastrophe modeling loss outputs including Average Annual Loss,
  loss exceedance curves (OEP/AEP), event loss tables (1,943 stochastic events), and
  spatial loss aggregations. Dataset represents industry-standard probabilistic flood
  risk assessment comparable to commercial catastrophe models.'
exposure:
- asset_type:
    description: Building stock in Freetown classified using the GEM GED4ALL schema.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_freetown_buildings
  metrics:
  - dimension: structure
    id: metric_building_count
    measurement:
      quantity_kind: count
      unit: count
  - dimension: content
    id: metric_building_tiv
    measurement:
      quantity_kind: currency
      unit: USD
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: River (fluvial) flood hazard map showing flood depth for a 1-in-20
        year return period event in Freetown, Sierra Leone. Undefended scenario without
        flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: river_flood_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_FLRF_RP20
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.05
          probability:
            span: 50
            value: 0.923
          return_period: 20
    - calculation_method: simulated
      description: River (fluvial) flood hazard map showing flood depth for a 1-in-50
        year return period event in Freetown, Sierra Leone. Undefended scenario without
        flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: river_flood_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_FLRF_RP50
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability:
            span: 50
            value: 0.636
          return_period: 50
    - calculation_method: simulated
      description: River (fluvial) flood hazard map showing flood depth for a 1-in-100
        year return period event in Freetown, Sierra Leone. Undefended scenario without
        flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: river_flood_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_FLRF_RP100
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability:
            span: 50
            value: 0.395
          return_period: 100
    - calculation_method: simulated
      description: River (fluvial) flood hazard map showing flood depth for a 1-in-200
        year return period event in Freetown, Sierra Leone. Undefended scenario without
        flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: river_flood_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_FLRF_RP200
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.005
          probability:
            span: 50
            value: 0.222
          return_period: 200
    - calculation_method: simulated
      description: River (fluvial) flood hazard map showing flood depth for a 1-in-500
        year return period event in Freetown, Sierra Leone. Undefended scenario without
        flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: river_flood_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_FLRF_RP500
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.002
          probability:
            span: 50
            value: 0.095
          return_period: 500
    - calculation_method: simulated
      description: River (fluvial) flood hazard map showing flood depth for a 1-in-1500
        year return period event in Freetown, Sierra Leone. Undefended scenario without
        flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: river_flood_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_FLRF_RP1500
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000667
          probability:
            span: 50
            value: 0.033
          return_period: 1500
    frequency_distribution: null
    hazards:
    - classification: null
      id: river_flood_hazard_ref
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_river_flood
    occurrence_range: Return periods from 20, 50, 100, 200, 500, and 1,500 years
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Surface water (pluvial) flood hazard map showing flood depth for
        a 1-in-20 year return period event in Freetown, Sierra Leone. Undefended scenario
        without drainage systems or flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: surface_water_flood_hazard_ref
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_FLSW_RP20
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.05
          probability:
            span: 50
            value: 0.923
          return_period: 20
    - calculation_method: simulated
      description: Surface water (pluvial) flood hazard map showing flood depth for
        a 1-in-50 year return period event in Freetown, Sierra Leone. Undefended scenario
        without drainage systems or flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: surface_water_flood_hazard_ref
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_FLSW_RP50
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability:
            span: 50
            value: 0.636
          return_period: 50
    - calculation_method: simulated
      description: Surface water (pluvial) flood hazard map showing flood depth for
        a 1-in-100 year return period event in Freetown, Sierra Leone. Undefended
        scenario without drainage systems or flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: surface_water_flood_hazard_ref
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_FLSW_RP100
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability:
            span: 50
            value: 0.395
          return_period: 100
    - calculation_method: simulated
      description: Surface water (pluvial) flood hazard map showing flood depth for
        a 1-in-200 year return period event in Freetown, Sierra Leone. Undefended
        scenario without drainage systems or flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: surface_water_flood_hazard_ref
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_FLSW_RP200
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.005
          probability:
            span: 50
            value: 0.222
          return_period: 200
    - calculation_method: simulated
      description: Surface water (pluvial) flood hazard map showing flood depth for
        a 1-in-500 year return period event in Freetown, Sierra Leone. Undefended
        scenario without drainage systems or flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: surface_water_flood_hazard_ref
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_FLSW_RP500
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.002
          probability:
            span: 50
            value: 0.095
          return_period: 500
    - calculation_method: simulated
      description: Surface water (pluvial) flood hazard map showing flood depth for
        a 1-in-1500 year return period event in Freetown, Sierra Leone. Undefended
        scenario without drainage systems or flood defenses.
      disaster_identifiers: []
      hazard:
        classification: null
        id: surface_water_flood_hazard_ref
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_FLSW_RP1500
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.000667
          probability:
            span: 50
            value: 0.033
          return_period: 1500
    frequency_distribution: null
    hazards:
    - classification: null
      id: surface_water_flood_hazard_ref
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_surface_water_flood
    occurrence_range: Return periods from 20, 50, 100, 200, 500, and 1,500 years
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Flood impact assessment for Freetown, Sierra Leone, produced by JBA
    Risk Management using 2D (JFlow) and 1D (RFlow) hydraulic modelling. Flood inundation
    was derived from JBA global hydrological model outputs downscaled to Freetown's
    river network using the Intermap NEXTMap World30 Digital Surface Model as topographic
    input. Building exposure was based on the GEM Foundation GED4ALL Exposure Database
    disaggregated to a site-specific Freetown building portfolio. Flash flood observations
    from Freetown City Council were used for model validation. Loss was computed using
    proprietary JBA depth-damage vulnerability functions applied to building replacement
    values.
  sources:
  - id: source_jba_hydrology
    license: null
    name: JBA global hydrological models
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_nextmap_dsm
    license: null
    name: Intermap NEXTMap World30 DSM
    risk_data_type: null
    type: dataset
    url: https://www.intermap.com/nextmap
    used_in: hazard
  - id: source_jflow
    license: null
    name: JBA 2D hydraulic modeling software (JFlow)
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_rflow
    license: null
    name: JBA 1D hydraulic modeling software (RFlow)
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_gem_ged4all
    license: CC-BY-NC-SA-4.0
    name: GEM Foundation Global Seismic Risk Model - GED4ALL Exposure Database
    risk_data_type: null
    type: dataset
    url: https://www.globalquakemodel.org/gem
    used_in: exposure
  - id: source_freetown_portfolio
    license: CC-BY-NC-SA-4.0
    name: Freetown building portfolio (disaggregated exposure)
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_validation_floods
    license: null
    name: Freetown City Council flash flood observations
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
  - id: source_vulnerability_functions
    license: null
    name: Proprietary depth-damage vulnerability functions
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Average Annual Loss (AAL) for combined river and surface water flooding
      in Freetown study area. Total AAL: USD $808,905. Calculated from stochastic
      event set of 1,943 flood events using: (1) JBA probabilistic flood hazard maps
      at 1m resolution (6 return periods: RP20-RP1500), (2) GEM Foundation building
      exposure portfolio (153,436 buildings valued at USD $8.08 billion with GED4ALL
      taxonomy), and (3) proprietary depth-damage vulnerability functions. AAL represents
      expected annual building damage in ground-up losses. Vulnerability functions
      are commercial/proprietary and not included in this dataset but assumed to follow
      industry-standard depth-damage relationships for building types in GED4ALL taxonomy.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_aal_total
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: AAL disaggregated by occupancy classification. Residential buildings
      account for 98.6% of losses (USD $797,345 from 143,261 buildings), Commercial
      1.4% (USD $11,247 from 9,522 buildings), and Industrial 0.04% (USD $314 from
      652 buildings). High residential loss share reflects both higher building count
      and higher flood exposure in residential areas of Freetown.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_aal_by_occupancy
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: AAL aggregated by administrative district (Admin2 level). Western
      Area Urban district accounts for 73.5% of total AAL (USD $594,607) while Western
      Area Rural accounts for 26.5% (USD $214,300). Urban concentration reflects higher
      building density and exposure values in downtown Freetown.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_aal_by_district
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Spatial AAL dataset at Admin4 (ward/section) level provided as shapefile.
      74 wards with AAL ranging from USD $0 (3 wards) to USD $144,276 (Gloucester
      ward, highest risk). Total AAL: USD $815,504 (slight difference from probabilistic
      total of USD $808,905 likely due to spatial aggregation methods). This spatial
      dataset enables ward-level investment prioritization and targeted risk reduction
      interventions.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_aal_spatial_admin4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Occurrence Exceedance Probability (OEP) curve showing ground-up
      flood losses at return periods from RP2 to RP1000. Key loss metrics: RP100 =
      USD $13.46M (1% annual probability, regulatory standard), RP500 = USD $60.37M
      (0.2% annual probability, common insurance threshold), RP1000 = USD $82.63M
      (Probable Maximum Loss). OEP represents the maximum loss from a single event
      in a given year at each return period. Used for regulatory capital calculations,
      Solvency II compliance, and insurance/reinsurance pricing decisions.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_oep_curve
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Aggregate Exceedance Probability (AEP) curve showing total annual
      aggregate losses at return periods from RP2 to RP1000. AEP accounts for possibility
      of multiple flood events occurring in same year, aggregating all event losses.
      Used for portfolio risk assessment and annual loss budgeting.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_aep_curve
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Event Loss Table (ELT) containing ground-up losses for 1,943 stochastic
      flood events representing full range of possible flood scenarios. Maximum single
      event loss: USD $135.4 million. Mean event loss: USD $4.16 million. 1,775 events
      (91.4%) produce non-zero losses. Used for reinsurance pricing, catastrophe bond
      modeling, and risk transfer calculations.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_elt
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Period Loss Table (PLT) showing annual loss distributions across
      simulated years. Each year contains one or more stochastic events sampled from
      full event set. Used by risk managers and CFOs for financial planning, capital
      allocation, and understanding year-to-year loss volatility.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_freetown_plt
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'National Average Annual Loss for Sierra Leone. Total national AAL:
      USD $101.3 million. By province: Eastern USD $31.6M (31.2%), Southern USD $29.3M
      (29.0%), North West USD $20.5M (20.2%), Northern USD $17.8M (17.6%), Western
      Area USD $2.1M (2.1%). By occupancy: Residential USD $99.0M (97.8%), Commercial
      USD $2.2M (2.1%), Industrial USD $103K (0.1%). Freetown represents only 0.8%
      of national AAL. Complete probabilistic outputs (OEP, AEP, ELT, PLT) available
      at national, provincial, and district levels.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_sle_national_aal
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
project:
  name: 'Selection # 1279998 / Consultancy Services to develop capacities and capabilities
    in relation to climate, weather and disaster risk management services in Sierra
    Leone'
  url: https://www.worldbank.org
publisher:
  affiliation: null
  email: data@gfdrr.org
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support the Government of Sierra Leone and relevant stakeholders in understanding
  comprehensive flood risk, enabling evidence-based investment decisions, insurance/reinsurance
  pricing, and disaster risk management planning for Freetown.
referenced_by: []
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0066934/freetown-sierra-leone-flood-risk-assessment
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Complete set of high-resolution (1m) probabilistic flood hazard maps\
    \ for Freetown covering both river (fluvial) and surface water (pluvial) flooding.\
    \ Data formats: GeoTIFF (primary raster data), PDF (methodology documentation),\
    \ XML (metadata), OVR (overview pyramids). Contains 12 GeoTIFF rasters (6 return\
    \ periods \xC3\u2014 2 flood types) in WGS84 (EPSG:4326). File naming convention:\
    \ Freetown_202304_{FLRF|FLSW}_U_RP{20|50|100|200|500|1500}_RD_1m_4326.tif where\
    \ FLRF=River Flood, FLSW=Surface Water Flood, U=Undefended. Each GeoTIFF includes\
    \ auxiliary XML metadata and overview (OVR) files. Also includes 2 technical methodology\
    \ PDFs (JBA_Freetown_Sierra_Leone_RiverFloodMap2023.pdf and JBA_Freetown_Sierra_Leone_SurfaceWaterFloodMap2023.pdf)\
    \ documenting modeling approach, hydrological/hydraulic models (JFlow 2D + RFlow\
    \ 1D for river, JFlow 2D only for surface water), data sources (Intermap NEXTMap\
    \ World30 DSM), and model specifications. Flood depth rasters enhanced from 30m\
    \ base resolution to 1m using water filling algorithm. Undefended scenarios model\
    \ flooding without flood defenses or drainage systems."
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095923/2023s0512_Freetown_Flood_Hazard_Maps.zip
  format: null
  id: resource_freetown_hazard_maps
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Freetown Flood Hazard Maps
- access_url: https://datacatalog.worldbank.org/search/dataset/0066934/freetown-sierra-leone-flood-risk-assessment
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Spatial loss datasets and visualization products for Freetown flood
    risk. Data formats: Shapefile (primary spatial data with .shp, .shx, .dbf, .prj,
    .cpg components), PDF (visualization maps). Primary dataset is Admin4-level AAL
    shapefile (Freetown_Admin4_Combined_Flood_AAL.shp) containing Average Annual Loss
    in USD for 74 wards/sections, with values ranging from $0 to $144,276 per ward
    (total AAL: $815,504). Includes 6 PDF visualization maps: AAL choropleth map,
    topographic overview, and RP20/RP100 flood hazard maps (with and without observed
    flood points). Also contains City Council validation data: flash flood observation
    points shapefile (45 locations) and flash flood areas shapefile (8 polygons) used
    for model ground-truthing. Additional vector datasets include RP20 and RP100 flood
    extent polygons. All shapefiles in WGS84 (EPSG:4326) with complete attribute tables.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095922/2023s0512_Freetown_Flood_Hazard_and_Loss_Maps.zip
  format: null
  id: resource_freetown_loss_maps
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Freetown Flood Hazard and Loss Maps
- access_url: https://datacatalog.worldbank.org/search/dataset/0066934/freetown-sierra-leone-flood-risk-assessment
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Complete catastrophe modeling outputs for Freetown including Average
    Annual Loss (AAL), Occurrence Exceedance Probability (OEP), Aggregate Exceedance
    Probability (AEP), Event Loss Tables (ELT), and Period Loss Tables (PLT). Data
    formats: CSV (primary probabilistic outputs), TXT (summary documentation). Contains
    15 CSV files organized by aggregation level: S1 (by occupancy: residential/commercial/industrial),
    S2 (by study area: Freetown 1m DEM extent), S3 (by district: Western Area Urban/Rural).
    File naming convention: 2023s0512_SLE_Freetown_03_gul_{S1|S2|S3}_{aalcalc|eltcalc|leccalc_wheatsheaf_mean_aep|leccalc_wheatsheaf_mean_oep|pltcalc}.csv.
    Key results: Total AAL $808,905 USD, RP100 loss $13.46M, RP500 loss $60.37M, RP1000
    PML $82.63M. ELT contains 1,943 stochastic flood events with maximum single event
    loss of $135.4M. Includes summary text file explaining aggregation levels and
    methodology. Ground-up losses calculated from JBA hazard maps, GEM exposure portfolio
    (153,436 buildings), and proprietary vulnerability functions.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095924/2023s0512_Freetown_Probabilistic_Analysis_Results.zip
  format: null
  id: resource_freetown_probabilistic
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Freetown Probabilistic Analysis Results
- access_url: https://datacatalog.worldbank.org/search/dataset/0066934/freetown-sierra-leone-flood-risk-assessment
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Building exposure datasets used for flood loss modeling. Data formats:
    CSV (primary exposure data), TXT (license and documentation). Contains GEM Foundation
    GED4ALL (Global Exposure Database for All) national data for Sierra Leone: Exposure_Res_Sierra_Leone.csv
    (336 records, 883,521 residential buildings, $38.3B USD), Exposure_Com_Sierra_Leone.csv
    (147 records, 39,418 commercial buildings, $3.0B USD), Exposure_Ind_Sierra_Leone.csv
    (84 records, 3,178 industrial buildings, $288.8M USD). GED4ALL data includes building
    taxonomy, replacement costs, dwelling counts, and occupants per asset at Admin1/Admin2
    levels. Primary loss modeling dataset is Freetown_ptf_v2.csv containing 153,436
    disaggregated building records with precise lat/lon coordinates, Total Insurable
    Value (TIV) in USD, occupancy codes (1050=Residential, 1100=Commercial, 1150=Industrial),
    and peril coverage codes (ORF=River Flood, OSF=Surface Water Flood). Total Freetown
    exposure: $8.08B USD. Also includes SLE_admin2_ptf_output.csv (complete Sierra
    Leone portfolio at Admin2 level). README.txt documents GEM Foundation license
    (CC-BY-NC-SA 4.0) and data lineage from Global Seismic Risk Model.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095925/2023s0512_Modelled_Exposure.zip
  format: null
  id: resource_modelled_exposure
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Modelled Exposure Data
- access_url: https://datacatalog.worldbank.org/search/dataset/0066934/freetown-sierra-leone-flood-risk-assessment
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National-level flood risk visualization products for Sierra Leone
    showing Average Annual Loss (AAL) aggregated at different administrative and economic
    levels. Data formats: PDF (primary cartographic products), PNG (AAL by occupancy
    chart). Contains 3 PDF maps and 1 PNG: AAL by province (Admin1: 5 provinces),
    AAL by district (Admin2: 16 districts), AAL by line of business/occupancy (residential/commercial/industrial),
    and national overview. Maps show spatial distribution of USD $101.3M total national
    AAL with provincial breakdown: Eastern $31.6M (31.2%), Southern $29.3M (29.0%),
    North West $20.5M (20.2%), Northern $17.8M (17.6%), Western Area $2.1M (2.1%).
    Cartographic products complement the probabilistic analysis CSV outputs and enable
    strategic national-level flood risk planning.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095926/2023s0512_Sierra_Leone_Flood_Loss_Maps.zip
  format: null
  id: resource_sle_loss_maps
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sierra Leone National Flood Loss Maps
- access_url: https://datacatalog.worldbank.org/search/dataset/0066934/freetown-sierra-leone-flood-risk-assessment
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Complete national-level catastrophe modeling outputs for Sierra Leone
    including AAL, OEP, AEP, ELT, and PLT at four aggregation levels. Data formats:
    CSV (primary probabilistic outputs), TXT (summary documentation). Contains 20
    CSV files organized as: S1 (national total), S2 (by district/Admin2: 16 districts),
    S3 (by occupancy: residential/commercial/industrial), S4 (by province/Admin1:
    5 provinces). File naming convention: 2023s0512_Sierra Leone_05_gul_{S1|S2|S3|S4}_{aalcalc|eltcalc|leccalc_wheatsheaf_mean_aep|leccalc_wheatsheaf_mean_oep|pltcalc}.csv.
    Key results: National AAL $101.3M USD, occupancy breakdown showing 97.8% residential
    ($99.0M), 2.1% commercial ($2.2M), 0.1% industrial ($103K). Complete stochastic
    event sets and loss distributions enable national-level portfolio risk assessment,
    reinsurance pricing, and disaster risk financing. Includes summary text file documenting
    aggregation structure. Freetown (Western Area) represents only 0.8% of national
    AAL, indicating significant rural and other urban flood risk exists across Sierra
    Leone.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095927/2023s0512_Sierra_Leone_Probabilistic_Analysis_Results.zip
  format: null
  id: resource_sle_probabilistic
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sierra Leone National Probabilistic Analysis Results
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sle_freetownfloodrisk
spatial:
  bbox:
  - -13.303192
  - 8.3417096
  - -13.115017
  - 8.5038197
  centroid: null
  countries:
  - SLE
  gazetteer_entries:
  - description: Freetown
    id: gazetteer_freetown
    scheme: GEONAMES
    uri: https://www.geonames.org/2409306/freetown.html
  scale: sub-national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Comprehensive Flood Risk Assessment for Freetown, Sierra Leone
version: '1.0'
vulnerability: null
---
