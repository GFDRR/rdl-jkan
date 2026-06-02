---
catalog: null
contact_point:
  email: null
  id: attribution_editor
  name: Eugenio Chioccarelli (Univ. Mediterranea di Reggio Calabria), Iunio Iervolino
    (Univ. di Napoli Federico II)
  url: https://www.reluis.it/en/rintc-dff/
creator:
  email: null
  id: attribution_creator
  name: ReLUIS Working Group WP3 (2014-2022)
  url: https://www.reluis.it/en/rintc-dff/
dataset_id: rdls_vln-ita_reluis_rintcfragility
description: 'Lognormal seismic fragility functions for Italian buildings and bridges,
  developed under the RINTC project (Implicit Seismic Risk of Code-Conforming Structures,
  2014-2022). The database contains 647 fragility function entries covering five construction
  material types (unreinforced masonry, reinforced concrete, base-isolated RC, precast
  concrete, steel) and bridges. Functions are provided for both code-conforming structures
  (designed per NTC2008/NTC2018) and existing/retrofitted structures (designed per
  previous Italian codes from pre-1920 to 1990s). Each function is parameterised as
  a lognormal distribution (median eta and dispersion beta) for two performance levels:
  Usability Preventing Damage (UPD) and Global Collapse (GC) or Severe Damage (SD
  for bridges). Intensity measures are spectral accelerations Sa(T) at periods from
  0.15s to 3.0s. Over 300 structures were analysed at five representative Italian
  sites (L''Aquila, Catania, Naples, Rome, Milan) with varying seismic hazard levels
  using nonlinear dynamic analysis of 3D numerical models.'
details: 'Fragility functions were derived from nonlinear dynamic analyses of three-dimensional
  numerical models. The database is organised in 11 data sheets: code-conforming and
  evolution (existing/retrofitted) sheets for each of URM (90+50 entries), RC (84+144),
  BI (12+24), PRC (51+26), Steel (96+40), plus Bridges (30). Structural metadata includes
  construction material, design code era, design PGA, site, soil class, number of
  stories, regularity, and structural details specific to each type. Curve fitting
  methods include Maximum Likelihood (ML), Normal Probability Plot (NPP), Least Squares
  Fitting (LSF), and Direct assignment (D). URM entries include 13 masonry subtypes;
  RC entries distinguish moment-resisting frames from shear walls with optional soil-structure
  interaction; BI entries specify isolation system type (FPS, HDRB, HDRB+S); PRC entries
  specify beam-column connection and cladding type; Steel entries include plan dimensions
  and bracing configuration; Bridge entries specify structural typology, pier characteristics,
  and height.'
exposure: null
extra_attributions:
- email: null
  id: attribution_funder
  name: Italian Department of Civil Protection (DPC)
  role: funder
  url: https://www.protezionecivile.gov.it
hazard: null
license: CC-BY-ND-4.0
loss: null
project:
  name: RINTC - Implicit Seismic Risk of Code-Conforming Structures (ReLUIS-DPC 2014-2022)
  url: https://www.reluis.it/en/rintc-dff/
publisher:
  email: null
  id: attribution_publisher
  name: ReLUIS - Rete dei Laboratori Universitari di Ingegneria Sismica
  url: https://www.reluis.it
purpose: Quantification of the implicit seismic risk (annual failure rate) of Italian
  structures designed according to current and past Italian building codes, enabling
  comparison of seismic performance across design eras and structural types.
resources:
- coordinate_system: null
  description: 'Single Excel workbook containing 647 lognormal fragility function
    entries across 11 data sheets, plus About and Format documentation sheets. Data
    sheets are organised by construction material (URM, RC, BI, PRC, Steel, Bridges)
    and design category (code-conforming vs evolution/existing). Each entry provides:
    structural metadata (material, masonry type, design code/era, design PGA, site,
    soil class, stories, regularity, structural details), analysis metadata (performance
    level, curve fitting method, intensity measure), fragility parameters (eta median
    in g, beta dispersion), and publication references with hyperlinks. Intensity
    measures: Sa(0.15s) to Sa(3.0s). Performance levels: UPD (Usability Preventing
    Damage), GC (Global Collapse), SD (Severe Damage for bridges).'
  download_url: https://www.reluis.it/en/rintc-dff/
  format: Excel (xlsx)
  id: resource_rintc_database
  media_type: null
  spatial_resolution: null
  temporal: null
  title: RINTC Database of Fragility Functions (Excel)
risk_data_type:
- vulnerability
schema: rdl-03
slug: rdls_vln-ita_reluis_rintcfragility
spatial:
  countries:
  - ITA
  scale: national
title: RINTC Database of Fragility Functions v1.0 (beta) - Italian Seismic Building
  and Bridge Fragility
version: 1.0-beta
vulnerability:
  approach: analytical
  base_data_type: simulated
  category: buildings, infrastructure
  dimension: ''
  function_type: ''
  hazard_analysis_type: probabilistic
  hazard_primary: earthquake
  hazard_process_primary: ground_motion
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: probability
  relationship: math_parametric
  taxonomy: Custom
  unit: ''
---
